import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Idea :
        # n = len(piles)
        # Create a function f such that R^n x R --> R 
        # takes the plies and interger and gives a time H
        # if k = max(piles) --> f(p, max(piles)) = n = H_min
        # if k = 1 --> f(p, max(piles)) = sum(piles) = H_max
        # Since f(p,k) is a non increasing function with k
        # Binary search from k = 1 up to k = max(piles)
        
        # Create f
        def f(piles, k):
            return  sum ( [ math.ceil(p / k) for p in piles ] )

        k_min = 1
        k_max = max(piles)

        # assert feasibility
        if k_min <= 0 or f(piles, k_max) > h:
            return
        
        if f(piles, k_min) < h:
            return k_min 

        
        # Binary search
        L = k_min
        R = k_max
        res = k_max

        while L <= R :

            mid = ( L + R ) // 2

            if f(piles, mid) > h :
                L = mid + 1
            else :
                res = min(res, mid)
                R = mid - 1
        
        return res





        