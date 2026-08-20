# Optimal solution
# First create a set of unique number to avoid repetition
# start counting only if number - 1 not in the set
# TC : O(n)
# SC : O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        res = 1

        for number in set(nums) :
            if number - 1 not in set(nums):
                curr = 1
                while number + 1 in set(nums):
                    curr = curr + 1
                    number = number + 1
                res = max(res, curr)


        return res















        
        