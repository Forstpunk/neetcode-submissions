from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max((num for num in count if count[num] == 1), default=-1)
        
        