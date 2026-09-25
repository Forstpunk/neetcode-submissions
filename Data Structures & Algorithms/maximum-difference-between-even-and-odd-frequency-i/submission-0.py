class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        
        max_odd  = 0
        min_even = float('inf')    # start very large
        
        for count in freq.values():
            if count % 2 != 0:     # odd frequency
                max_odd  = max(max_odd,count)
            else:                   # even frequency
                min_even = min(min_even, count)
        
        return max_odd - min_even