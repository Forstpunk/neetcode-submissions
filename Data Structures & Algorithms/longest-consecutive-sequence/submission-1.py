class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for i in num_set:
            if i-1 not in num_set:
                streak =1
                while i + streak in num_set:
                    streak +=1
                best = max(best,streak)
        return best  
        