#include <vector>
#include <algorithm>

class Solution {
public:
    int uniqueXorTriplets(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<int> unique_nums;
        for (int num : nums) {
            if (unique_nums.empty() || unique_nums.back() != num) {
                unique_nums.push_back(num);
            }
        }
        const int MAX_XOR = 2048; 
        std::vector<bool> pairs_xor(MAX_XOR, false);
        std::vector<bool> triplets_xor(MAX_XOR, false);
        for (size_t i = 0; i < unique_nums.size(); ++i) {
            for (size_t j = i; j < unique_nums.size(); ++j) {
                pairs_xor[unique_nums[i] ^ unique_nums[j]] = true;
            }
        }
        for (int num : unique_nums) {
            for (int val = 0; val < MAX_XOR; ++val) {
                if (pairs_xor[val]) {
                    triplets_xor[val ^ num] = true;
                }
            }
        }
        int unique_count = 0;
        for (int val = 0; val < MAX_XOR; ++val) {
            if (triplets_xor[val]) {
                unique_count++;
            }
        }

        return unique_count;
    }
};
