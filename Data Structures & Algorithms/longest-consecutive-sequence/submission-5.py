# Brute force sol
# for each number in nums, check if the next number is inside nums
# if it is, increase the counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if  len(nums) == 0 or len(nums) == 1:
            return len(nums)

        res = 0

        for number in nums:
            curr = 1
            while number + 1 in nums:
                curr = curr + 1
                number = number + 1
            res = max(res, curr)    

        return res







        
        