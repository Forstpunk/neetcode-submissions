from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num =Counter(nums)
        for i in range(len(nums)):
            if num[nums[i]] > len(nums)//2:
                return nums[i]

        