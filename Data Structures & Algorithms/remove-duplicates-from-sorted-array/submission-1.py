class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1            # start here

        for i in range(1,len(nums)):    # start loop here
            if nums[i] != nums[i-1]:             # keep condition
                nums[k] = nums[i]
                k += 1

        return k