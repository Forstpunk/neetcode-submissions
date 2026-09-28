from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f = Counter(text)
        return min(f['b'],f['a'],f['l']//2,f['o']//2,f['n'])
        