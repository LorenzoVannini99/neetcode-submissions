from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len ( nums )

        if n == 0 :
            return []

        if n == 1 :
            return [nums[0]]

        h = Counter ( nums )

        l_sorted = sorted (h.items() , key = lambda item : item[1] , reverse = True)         
        
        res = [key for key,value in l_sorted[:k]]

        return res