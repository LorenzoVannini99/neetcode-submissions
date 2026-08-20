# Brute force Solution :
# two nested for
# for each number check if it's inside the nums
# n + n-1 + n-2... = = O(n^2)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums or len(nums) == 1:
            return False

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] == nums[j]:
                        return True
    
        return False

# TC : O(n^2)
# SC : O(1)