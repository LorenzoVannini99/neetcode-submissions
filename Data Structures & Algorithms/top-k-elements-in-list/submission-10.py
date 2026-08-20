
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
       
        # n = nums length
        # m <= n = number of unique elements in nums

        count = Counter ( nums ) # count[number] = freq

        min_heap = []

        heapq.heapify(min_heap)

        for number,freq in count.items():

            heapq.heappush(min_heap, (freq, number))

            if len(min_heap) > k:
                heapq.heappop(min_heap) 

        # here, we have k tuples containing (freq, number)
        return [ number for _ , number in min_heap ]











