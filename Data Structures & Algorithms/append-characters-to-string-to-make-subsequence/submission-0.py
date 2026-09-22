class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return len(t) - i    # ← only this line changes from isSubsequence