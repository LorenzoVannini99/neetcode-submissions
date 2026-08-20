# Minheap solution
from collections import Counter
import heapq
# use a Counter but keep only the most k freq element
# n = len(nums)
# m = unique numbers
# TC : O(n + mlogk) < O(n + mlogm) if m < k
# SC : O( m )
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = Counter(nums)
        heap = []

        for number, freq in d.items():
            heapq.heappush(heap, (freq, number)) # log(k)
            if len(heap) > k:
                heapq.heappop(heap) # log(k)

        return [ number for _ , number in heap]    
        



