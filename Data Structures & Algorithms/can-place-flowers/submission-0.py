class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left  = flowerbed[i-1] if i > 0 else 0           # left neighbor
            right = flowerbed[i+1] if i < len(flowerbed)-1 else 0  # right neighbor
            
            if flowerbed[i] == 0 and left == 0 and right == 0:
                flowerbed[i] = 1    # plant here
                n -= 1              # one fewer to place
                if n == 0:
                    return True
        
        return n <= 0