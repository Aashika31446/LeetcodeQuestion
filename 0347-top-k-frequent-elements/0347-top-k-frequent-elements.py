from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        answer = heapq.nlargest(k, freq.keys(), key=freq.get)
        return answer
