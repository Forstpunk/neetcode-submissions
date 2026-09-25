class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(len(nums)):      # check every element
            if nums[i] != val:
                nums[c] = nums[i]       # place valid element
                c += 1
        return c