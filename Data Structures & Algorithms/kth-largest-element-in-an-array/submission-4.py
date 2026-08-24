# Optimal sol:

# We do not need to sort everything
# We only need the kth largest element

# We can use a min_heap
# If I use a min heap i can store the kth largest element
# everytime the length of the min heap is greater than k
# I pop the last k+1 element, the smallest so far
# so I keep from k +1 the largest k element
# and so on

# TC : O(n * log(k))
# SC : O(n + k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq

        min_heap = []
        heapq.heapify(min_heap)

        for number in nums:

            heapq.heappush(min_heap, number)

            if len(min_heap) > k :
                heapq.heappop(min_heap) # O(log k)

        # Here I have the k largest element
        # In a heap no ordering is guaranteed beside the first element
        # the first element [0] is the smallest
        return min_heap[0]

        