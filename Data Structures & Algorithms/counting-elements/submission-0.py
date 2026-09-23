class Solution:
    def countElements(self, arr: list) -> int:
        arr_set = set(arr)    # separate set — keeps arr intact
        count = 0
        
        for x in arr:                  # loop original arr (with duplicates)
            if (x + 1) in arr_set:     # does x+1 exist?
                count += 1
        
        return count