class StringIterator:
    def __init__(self, compressedString: str):
        self.pairs = []
        i = 0
        while i < len(compressedString):
            char = compressedString[i]
            i += 1
            num_start = i
            while i < len(compressedString) and compressedString[i].isdigit():
                i += 1
            count = int(compressedString[num_start:i])
            self.pairs.append((char, count))
        
        self.index = 0
        self.remaining = 0
        self.current_char = " "
        
        if self.pairs:
            self.current_char = self.pairs[0][0]
            self.remaining = self.pairs[0][1]
            self.index = 1
    
    def next(self) -> str:
        if not self.hasNext():
            return " "
        if self.remaining == 0:
            self.current_char = self.pairs[self.index][0]
            self.remaining = self.pairs[self.index][1]
            self.index += 1
        self.remaining -= 1
        return self.current_char
    
    def hasNext(self) -> bool:
        return self.remaining > 0 or self.index < len(self.pairs)