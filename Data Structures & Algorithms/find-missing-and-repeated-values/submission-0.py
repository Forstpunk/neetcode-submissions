from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        f = Counter(j for i in grid for j in i)
        repeated = 0
        missing = 0
        n = len(grid)
        
        for num in range(1, n*n + 1):    # check ALL numbers 1 to n²
            if f[num] == 2:
                repeated = num
            elif f[num] == 0:
                missing = num
        
        return [repeated, missing]