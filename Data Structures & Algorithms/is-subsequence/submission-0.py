class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0    # pointer for s
        j = 0    # pointer for t
        
        while i< len(s) and j< len(t):      # blank 1: both pointers in bounds
            if s[i] == t[j]:
                i +=1
                j +=1            # blank 2: match → move both
            else:
                j +=1           # blank 3: no match → move only j
        
        return i == len(s)    # blank 4: success condition
        