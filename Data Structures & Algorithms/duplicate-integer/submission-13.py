# Counter solution
# n = len(nums)
# Create a Counter
# If there is a value > 1 return False else return True
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums or len(nums) == 1:
            return False
        
        from collections import Counter

        d = Counter(nums)

        for value in d.values():
            if value > 1 :
                return True
        
        return False
        # TC : O(n + n)
        # SC : O(n)
        