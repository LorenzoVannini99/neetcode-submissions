
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
       n = len(piles)
       M = max(piles)
       m = min (piles)
      
       L = 1
       R = M

     
       def f(piles, k):
            return sum([math.ceil(p/k) for p in piles]) 


     
       while L < R :
            mid = (L + R) // 2
            if f(piles, mid) > h:
                L = mid + 1
            else :
                R = mid

       return  L
     


     


        