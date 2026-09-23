class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        string = {value: index for index, value in enumerate(keyboard)}
        total = 0
        current = 0
        
        for n in word:
            next_pos = string[n]              # find where this key is
            total += abs(current - next_pos)  # add distance traveled
            current = next_pos                # finger moves to new key
        
        return total