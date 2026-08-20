# Brute Force solution
# n = len(nums)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return 
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # TC : O(n^2)
        # SC : O(1)