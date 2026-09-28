class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        o = []
        for i in range(1,len(nums)+1):
            if i not in nums:
                o.append(i)
        return o 

            
        