
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # n = nums length
        # m <= n = number of unique elements in nums

        # Idea :
        # Use the Counter
        # then use a min heap to improve performances
        # if you have k + 1 elements, by using a minheap, you pop in (Ologn)  the smallest
        # so you have the k biggest number

        # TC : O(n)
        # SC : O(m)
        counter_dict = Counter ( nums )
        
        heap = []

        for number in counter_dict.keys() :
            
            heapq.heappush(heap, (counter_dict[number], number)) # TC : O(logk)
            
            if len(heap) > k:
                heapq.heappop(heap) # TC : O(logk)

        return [ number for _ ,number in heap ]
        

        









