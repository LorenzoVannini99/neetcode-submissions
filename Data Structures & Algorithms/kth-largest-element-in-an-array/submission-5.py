"""
Naive solution :

if k != 1 or k != len(nums)

Sort and return sorted(nums)[-k]

otherwise
if k == 1 return max(nums) --> O(n)
if k == len(nums) return min(nums) --> O(n) 

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if k == 1:
            return max(nums)
        elif k == len(nums):
            return min(nums)

        else:

            return sorted(nums)[-k]

        

        
        