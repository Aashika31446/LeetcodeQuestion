class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_val=max(nums)
        min_val=min(nums)
        freq=[0]*(max_val-min_val+1)
        for s in nums:
            freq[s-min_val]+=1
        for i in range(len(freq)-1,-1,-1):
            k-=freq[i]
            if k<=0:
                return i+min_val