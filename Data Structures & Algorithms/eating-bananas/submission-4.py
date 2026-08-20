import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eating_time ( k ) :
            if k > 0 :
                return sum ( [math.ceil (p / k) for p in piles ] )
        
        n = len ( piles )
        l = 1
        r = max ( piles )

        while l < r :

            mid = ( l + r ) // 2

            if eating_time (mid) > h :
                l = mid + 1
            else :
                r = mid         
        
        return l
        




   





        