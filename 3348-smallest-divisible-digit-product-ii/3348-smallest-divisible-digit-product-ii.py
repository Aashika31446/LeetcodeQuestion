from typing import List


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        digit_factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        # Factorize t into 2^a * 3^b * 5^c * 7^d
        x = t
        required = []

        for prime in (2, 3, 5, 7):
            count = 0

            while x % prime == 0:
                x //= prime
                count += 1

            required.append(count)

        # No zero-free digit product can contain other prime factors.
        if x != 1:
            return "-1"

        need2, need3, need5, need7 = required

        # Precompute the minimum number of digits needed
        # to cover powers of 2 and 3.
        min_23 = [
            [0] * (need3 + 1)
            for _ in range(need2 + 1)
        ]

        for a in range(need2 + 1):
            for b in range(need3 + 1):
                best = float("inf")

                # Use digit 6 to cover one factor 2 and one factor 3.
                for sixes in range(min(a, b) + 1):
                    remaining_2 = a - sixes
                    remaining_3 = b - sixes

                    digits_for_2 = (remaining_2 + 2) // 3
                    digits_for_3 = (remaining_3 + 1) // 2

                    best = min(
                        best,
                        sixes + digits_for_2 + digits_for_3
                    )

                min_23[a][b] = best

        def min_digits(req):
            a, b, c, d = req
            return min_23[a][b] + c + d

        def consume(req, digit):
            factors = digit_factors[digit]

            return tuple(
                max(0, req[i] - factors[i])
                for i in range(4)
            )

        def build_suffix(req, length):
            if min_digits(req) > length:
                return None

            result = []

            for pos in range(length):
                slots_left = length - pos - 1

                # Greedily choose the smallest possible digit.
                for digit in range(1, 10):
                    next_req = consume(req, digit)

                    if min_digits(next_req) <= slots_left:
                        result.append(str(digit))
                        req = next_req
                        break

            return "".join(result)

        n = len(num)

        # Prefix factor counts.
        prefix = [[0, 0, 0, 0]]
        zero_free_prefix = [True]

        for ch in num:
            digit = int(ch)
            current = prefix[-1][:]

            if digit != 0:
                factors = digit_factors[digit]

                for i in range(4):
                    current[i] += factors[i]

            prefix.append(current)
            zero_free_prefix.append(
                zero_free_prefix[-1] and digit != 0
            )

        # Check whether num itself is already valid.
        if zero_free_prefix[n]:
            remaining = tuple(
                max(0, required[i] - prefix[n][i])
                for i in range(4)
            )

            if min_digits(remaining) == 0:
                return num

        # Try to make the number larger at the rightmost possible position.
        for i in range(n - 1, -1, -1):
            if not zero_free_prefix[i]:
                continue

            original_digit = int(num[i])
            prefix_factors = prefix[i]
            suffix_length = n - i - 1

            for digit in range(original_digit + 1, 10):
                factors = digit_factors[digit]

                remaining = tuple(
                    max(
                        0,
                        required[j]
                        - prefix_factors[j]
                        - factors[j]
                    )
                    for j in range(4)
                )

                if min_digits(remaining) <= suffix_length:
                    suffix = build_suffix(
                        remaining,
                        suffix_length
                    )

                    return (
                        num[:i]
                        + str(digit)
                        + suffix
                    )

        # No same-length solution exists.
        required_tuple = tuple(required)

        new_length = max(
            n + 1,
            min_digits(required_tuple)
        )

        return build_suffix(required_tuple, new_length)