from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque()    # sliding window of last 'size' elements
        self.total = 0           # running sum
    
    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.total -= self.window.popleft()    # remove oldest
        self.window.append(val)                    # add newest
        self.total += val                          # update sum
        return self.total / len(self.window)       # compute average