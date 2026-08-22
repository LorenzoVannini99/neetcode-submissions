
# Optimal solution: 
# Use a heap
# Idea :
# n = len(stones)
# Use a max heap, heapify something is in the order of O(n)
# so if we use a max heap --> costs n
# then pop twice using heappop()
# if you pop twice the biggest two elemments are popped
# if they are equal do nothing
# if they are not simply store and add this into the heap min
# popping cost is O(logn) --> O(2logn) = O(logn)
# adding is O(logn)
# so at the end is O(n)+ O(nlogn) = O(nlogn)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [ -s for s in stones]

        heapq.heapify(max_heap) # TC : O(n)

        while len(max_heap) > 1:
            y = heapq.heappop(max_heap) # O(log n)
            x = heapq.heappop(max_heap) # O(log n)

            if -y > -x:
                heapq.heappush(max_heap, (y - x) ) # O(log n)
        
        return -(max_heap[0]) if max_heap else 0



        