class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        r = nums[0]
        t = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                t +=nums[i]
            else:
                t = nums[i]
            r = max(r,t)
        return r 
        