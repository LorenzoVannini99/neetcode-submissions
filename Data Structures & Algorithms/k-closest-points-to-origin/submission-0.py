import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []

        def distance(p) :
            return math.sqrt( p[0] ** 2 + p[1] ** 2 )

        distances = [ (distance(p),p) for p in points ]
        heapq.heapify(distances)
        
        while len(res) < k :
            res.append(heapq.heappop(distances)[1])

        return res

            