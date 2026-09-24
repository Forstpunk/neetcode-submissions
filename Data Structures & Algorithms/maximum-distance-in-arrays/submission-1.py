class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        result = 0
        for i in range(1,len(arrays)):
            dist1 = global_max -  arrays[i][0]
            dist2 = arrays[i][-1] - global_min
            result  = max(result,dist1,dist2)

            global_min = min(global_min,arrays[i][0])
            global_max = max(global_max,arrays[i][-1])
        return result