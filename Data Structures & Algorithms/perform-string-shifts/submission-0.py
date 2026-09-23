class Solution:
    def stringShift(self, s: str, shift: list) -> str:
        # Step 1: calculate net shift
        net = 0
        for direction, amount in shift:
            if direction == 1:
                net += amount
            else:
                net -= amount
        
        # Step 2: reduce to within string length
        net = net % len(s)
        
        # Step 3: perform the shift
        return s[-net:] + s[:-net]