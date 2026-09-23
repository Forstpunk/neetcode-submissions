class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        s = str(n)
        rotated = ''
        
        for digit in s:
            if digit not in mapping:    # invalid digit → can't rotate
                return False
            rotated = mapping[digit] + rotated   # prepend → reverses order
        
        return rotated != s    # confusing only if different from original