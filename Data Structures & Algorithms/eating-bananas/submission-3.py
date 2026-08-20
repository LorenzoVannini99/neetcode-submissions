import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eating_time(k):
            return sum(math.ceil(p / k) for p in piles)
        
        l = 1
        r = max ( piles ) # TC : O(n)
        k_min = r 

        while l <= r :

            mid = ( l + r ) // 2

            if eating_time ( mid ) <= h :
                k_min = mid
                r = mid - 1
            else :
                l = mid + 1    

        return k_min



   





        