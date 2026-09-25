class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        o = [[1]]
        for i in range(1,numRows):
            prev =o[i-1]
            row = [1]
            for j in range(1,len(prev)):
                row.append(prev[j-1] + prev[j])
            row.append(1)
            o.append(row)
        return o


        