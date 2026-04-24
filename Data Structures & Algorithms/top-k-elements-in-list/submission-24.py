# SubOptimal
# MinHeap
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h = Counter(nums)

        min_heap = []
        heapq.heapify(min_heap)

        for number, occ in h.items():
            heapq.heappush(min_heap, (occ, number)) # TC : log(k)

            if len(min_heap) > k:
                heapq.heappop(min_heap) #  TC : log(k)

        return [number for _, number in min_heap ]


# TC : O( n + nlogk )
# SC : O(n + k)
        
        


