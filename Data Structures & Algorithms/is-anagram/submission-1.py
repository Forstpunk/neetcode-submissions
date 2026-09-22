class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: early exit
        if len(s) != len(t):
            return False
        
        # Step 2: build frequency map from s
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Step 3: decrement using t
        for char in t:
            count[char] = count.get(char, 0) - 1
            if count[char] < 0:
                return False
        
        # Only return True AFTER checking ALL characters
        return True