
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # n = len(nums)
        # m = unique elements
        # Counter and sort solution --> TC : O ( n + m + mlogm + k), SC: O(m)
        # Heap solution --> TC : O ( n + m*logk + k), SC: O(m + k)
        # Bucket sort -- > TC : O(n), SC: O(n)

        d = Counter(nums) 

        bucket = [ [] for _ in range(len(nums) + 1)]

        for number, freq in d.items():
            bucket[freq].append(number) 
        
        res = []
        for i in range(len(nums), -1, -1):
            for nums in bucket[i] :
                res.append(nums)

            if len(res) == k:
                return res



 





        
        












