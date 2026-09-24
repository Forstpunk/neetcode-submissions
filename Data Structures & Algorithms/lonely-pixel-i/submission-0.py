class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m,n = len(picture),len(picture[0])
        row_count = [0] * m 
        col_count = [0] * n

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_count[i] +=1
                    col_count[j] +=1
        result =0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row_count[i]==1 and col_count[j] ==1:
                    result +=1
        return result 