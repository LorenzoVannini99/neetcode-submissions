# Second solution:

# Suppose we cannot store in memory the n points
# we can use a cheaper solution but at a higher time complexity cost

# 2D plane, n points = [xi, yi]
# k closest point to the origin it means
# create a function f such that f(point) = distance
# f : R^2 -> R+
# f can be = sqrt(x**2 + y**2)
# sqrt can be slow so a simple f = x**2 + y**2 preserves the ordering

# use a max heap
# if you call n = len(points)
# Do not heapify straightforward everything
# just keep a max heap of length k
# extracting n-k times the closest point 
# SO TC : O( (n-k)* logk ) = O(n*logk)

# TC : O(n * logk) 
# SC : O(k)
# with k << n

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []
        res = []

        def distance(p):
            return p[0] ** 2 + p[1] ** 2
        
        import heapq

        heapq.heapify(max_heap)

        for p in points:

            d = distance(p)
            heapq.heappush( max_heap, [-d, p])

            if len(max_heap) > k :
                heapq.heappop(max_heap)

        return [elements[1] for elements in max_heap]





        