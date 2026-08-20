class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # O(n^2) solution

        for i in range(len(nums)- 1):
           for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
        
        return False

       
