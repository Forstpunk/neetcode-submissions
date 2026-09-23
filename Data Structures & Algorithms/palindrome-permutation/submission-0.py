from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # f = Counter(s)
        # return sum(1 for c in f.values() if c%2!=0)<=1
        f = Counter(s)
        return sum(1 for count in f.values() if count % 2 != 0) <= 1