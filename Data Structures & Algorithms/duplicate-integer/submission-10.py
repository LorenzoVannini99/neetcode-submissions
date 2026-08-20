# Sort solution
# n = len(nums)
# for each number
# check if something on the right appear more than once
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums or len(nums) == 1:
            return False
        
        nums_ordered = sorted(nums)

        for i in range(len(nums_ordered) - 1):
            if nums_ordered[i] == nums_ordered[i+1]:
                return True
        
        return False

        # TC : O(nlogn)
        # SC : O(1)
        