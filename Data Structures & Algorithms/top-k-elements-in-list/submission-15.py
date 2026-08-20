# Counter
from collections import Counter
# use a hashmap
# sort it and find the kth most frequent
# n = len(nums)
# m = unique numbers
# TC : O(n + )
# SC : O( m )
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if not nums :
            return []
        elif len(nums) == 1 :
            return nums    
        
        d = Counter(nums)
        sorted_d = sorted(d.items(), key = lambda x: x[1], reverse = True)

        return [numbers for numbers, freq in sorted_d[:k] ]



