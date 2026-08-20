# Brute Force solution
# n = len(nums)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums or len(nums) == 1:
            return False
        
        # for each number
        # check if something on the write appear more than once

        for i in range( len(nums) ):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False
        # TC : O(n^2)
        # SC : O(1)
        