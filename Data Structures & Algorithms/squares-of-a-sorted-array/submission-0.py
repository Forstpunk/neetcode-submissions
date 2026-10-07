class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n           # output array, filled right to left
        left, right = 0, n - 1
        pos = n - 1                # position to fill in result

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left]**2    # square the larger
                left += 1
            else:
                result[pos] = nums[right]**2    # square the larger
                right -= 1
            pos -= 1               # move position left

        return result