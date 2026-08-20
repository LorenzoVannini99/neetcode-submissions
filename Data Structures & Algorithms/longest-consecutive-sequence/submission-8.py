# Optimal solution
# First create a set of unique number to avoid repetition
# start counting only if number - 1 not in the set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        res = 1

        for number in s :
            if number - 1 not in s:
                curr = 1
                while number + 1 in s:
                    curr = curr + 1
                    number = number + 1
                res = max(res, curr)


        return res















        
        