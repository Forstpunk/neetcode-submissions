class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for k_idx in range(k):
                if mat1[i][k_idx] == 0:
                    continue              # skip zero rows — sparse optimization
                for j in range(n):
                    result[i][j] += mat1[i][k_idx] * mat2[k_idx][j]
        
        return result