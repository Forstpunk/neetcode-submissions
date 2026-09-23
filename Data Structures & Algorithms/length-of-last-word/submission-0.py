class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()          # remove trailing spaces
        r = 0
        for i in range(len(s)-1, -1, -1):   # scan right to left
            if s[i] == " ":     # hit a space → last word is done
                break
            r += 1              # count this character
        return r
        
        