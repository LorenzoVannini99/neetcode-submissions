# Brute force Solution
# Just check every possible pair of i,j indices
# if target is guaranteed to exist you will find one

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums or len(nums) == 1:
            return 
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# TC : O(n*n)
# SC : O(1)