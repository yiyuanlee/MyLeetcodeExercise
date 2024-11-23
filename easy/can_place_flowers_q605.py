from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spot = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0: 
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1  
                    spot += 1
                    if spot >= n:
                        return True
        
        return spot >= n
