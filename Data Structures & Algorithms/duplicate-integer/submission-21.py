# Optimal Solution :
# use a set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums or len(nums) == 1 or len(nums) == len(set(nums)):
            return False
        
        return True

# TC : O(n)
# SC : O(n)