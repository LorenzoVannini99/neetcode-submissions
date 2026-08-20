from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = Counter ( nums )

        d_sorted = sorted ( [(key,value) for key,value in d.items()] , key = lambda item: item[1], reverse = True )
        
        return [key[0] for key in d_sorted[:k]]

