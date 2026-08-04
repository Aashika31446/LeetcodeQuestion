class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for i in range(len(nums)-1):
            for x in range(nums[i]+1,nums[i+1]):
                res.append(x)
        return res
        