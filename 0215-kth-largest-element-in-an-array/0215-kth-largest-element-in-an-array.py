class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        while k:
            heap.append(nums.pop(0))
            k-=1
        heapq.heapify(heap)
        while nums:
            a=nums.pop(0)
            if a>heap[0]:
                heapq.heapreplace(heap,a)
        return heapq.heappop(heap)

        