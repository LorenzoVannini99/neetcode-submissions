import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eating_time(k: int) -> int:
            return sum(math.ceil(p / k) for p in piles)

        l = 1
        r = max(piles)
        min_k = r  # upper bound on answer

        while l <= r:
            mid = (l + r) // 2
            time = eating_time(mid)

            if time <= h:
                min_k = mid  # try to do better (smaller k)
                r = mid - 1
            else:
                l = mid + 1

        return min_k


        



   





        