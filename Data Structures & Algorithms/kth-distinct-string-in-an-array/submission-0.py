from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        count = 0
        
        for s in arr:
            if freq[s] == 1:      # distinct string
                count += 1
                if count == k:    # found the kth one
                    return s
        
        return ""    # fewer than k distinct strings