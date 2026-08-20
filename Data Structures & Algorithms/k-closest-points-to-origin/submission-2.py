import math
import heapq

# n is the number of points
# k the number of points to be returned
# n >= k

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(p):
            return (p[0] ** 2 + p[1] ** 2)

        # Using a max heap
        max_heap = []
        
        for p in points:
            d = dist(p)

            if len(max_heap) < k :
                heapq.heappush(max_heap , (-d,p) )
            else:
                heapq.heappush(max_heap , (-d,p))
                heapq.heappop(max_heap)

        res = []
        while max_heap:
            popped_item = heapq.heappop(max_heap)
            popped_points = popped_item[1]
            res.append(popped_points)

        return res    

        # TC : O ( n logk )
        # SC : O ( k )





