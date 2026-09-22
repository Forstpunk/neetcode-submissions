class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = -1
        for n in range(len(arr)-1,-1,-1):
            temp = arr[n]
            arr[n] = max_
            max_ = max(max_,temp)
        return arr

        