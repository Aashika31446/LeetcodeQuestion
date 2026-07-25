class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list1=[]
        currsum=0
        for i in range(0,len(nums)):
            currsum+=nums[i]
            list1.append(currsum)
        return list1


        