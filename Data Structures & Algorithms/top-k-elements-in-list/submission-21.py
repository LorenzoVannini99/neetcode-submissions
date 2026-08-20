# Sub Optimal
# use Counter 
# Then sort
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = Counter(nums)

        l = [(number, occurencies) for number, occurencies in hashmap.items() ]
        sorted_l = sorted(l, key = lambda x : x[1], reverse = True)

        return [number for number, _ in sorted_l[:k]]

# TC : O(n + n + nlog(n) + k) = O(nlogn)
# SC : O(n + n + n + k = = O(n)
        
        


