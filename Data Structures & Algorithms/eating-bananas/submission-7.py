import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Idea:
        # we have an array of length n of piles
        # piles = [ p1, p2, p3, ...] 
        # and h
        # which represents the number of hours you have to eat all the bananas.
        # You may decide your bananas-per-hour eating rate of k
        # piles = [1,4,3,2], h = 9
        # if k = 1 --> output = 10 > h XXXX WRONG
        # k = 2 --> you can eat the bananas in 6 hours
        #
        # In general with k = max(piles) -- > you can eat the bananas in n hours 
        # with k = 1 --> you can eat in sum(piles) hours
        # Since h > n , with k = max(piles) i am ok
        # I do not know if i am okay with k = 1 
        # This is the perfect case where binary search is used
        # Let's calculate f(piles, k) : R+ --> R+, the eating time
        # for a single pile p_i
        # if p_i % k == 0 --> time_i = (p_i \ k)
        # else --> time_i = (p_i \\ k) + 1 
        # or roundup ( p_i \ k )
        # T = sum_i time_i 
        # start with l = 1, r = Max(piles)
        # mid = (l+r) // 2
        # if f (piles, mid ) < h --> k_min = l = mid
        # else  f (piles, mid) > h --> r = mid - 1
        
        def eating_time(k) :
            return sum ( [ math.ceil( p / k) for p in piles ] )
        
        l = 1
        r = max( piles )
        
        while l < r :
            m = ( l + r) // 2

            if eating_time(m) <= h :
                r = m
            else:
                l = m + 1    
        
        return l




        