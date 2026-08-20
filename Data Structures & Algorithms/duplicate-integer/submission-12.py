# Hashmap solution
# n = len(nums)
# Create a set
# set look up is O(1)
# if number not in S add it
# if it is, there is a duplicate
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums or len(nums) == 1:
            return False
        
        S = set()

        for number in nums:
            if number not in S:
                S.add(number)
            else:
                return True  

        return False

        # TC : O(n)
        # SC : O(n)
        