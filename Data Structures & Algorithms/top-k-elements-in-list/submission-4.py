
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def Onklogk_sol():
            d = Counter(nums)
            d_sorted = sorted(d.items(), key=lambda item: item[1], reverse=True)
            return [key for key, _ in d_sorted[:k]]

        # O(n) bucket sort solution
        d = Counter(nums)  # Frequency map, O(n)
        bucket = [[] for _ in range(len(nums) + 1)]  # Bucket index = frequency

        for num, freq in d.items():
            bucket[freq].append(num)

        res = []
        for freq in range(len(nums), 0, -1):  # <-- FIXED THIS LINE
            for number in bucket[freq]:
                res.append(number)
                if len(res) == k:
                    return res







