# First solution:
# Suppose we can store in memory the n points
# we can use a asymptotically faster solution

# 2D plane, n points = [xi, yi]
# k closest point to the origin it means
# create a function f such that f(point) = distance
# f : R^2 -> R+
# f can be = sqrt(x**2 + y**2)
# sqrt can be slow so a simple f = x**2 + y**2 preserves the ordering
# use a max heap and pop everything k times
# if you call n = len(points)
# create a heap is O(n)
# extracting first k closest point is O(logm k) where m is the average min heap length 
# we can upper bound this to O(logn k)

# TC : O(n + k logn) 
# SC : O(n + k)
# with k << n

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        import heapq

        res = []

        def distance(p):
            return p[0] ** 2 + p[1] ** 2
        
        max_heap = [ (distance(p), p)  for p in points ] # TC : O(n)
        heapq.heapify(max_heap)

        while len(res) < k:
            last = heapq.heappop(max_heap)
            point = last[1]
            res.append(point)

        return res





        
        