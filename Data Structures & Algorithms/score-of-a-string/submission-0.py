class Solution:
    def scoreOfString(self, s: str) -> int:
        f = 0
        for i in range(len(s)-1):
            f = f+abs(ord(s[i])-ord(s[i+1]))
        return f


        