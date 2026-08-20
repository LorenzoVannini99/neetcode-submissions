# Idea:
# valid sub array if sum(sub_array) >= target
# TC : O(n)
# SC : O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if not nums:
            return 0
        
        L = 0
        R = 0
        curr_sum = 0
        res = len(nums) + 1

        while L <= R < len( nums ) :

            curr_sum += nums[R]

            while L <= R < len(nums) and curr_sum >= target:
                res = min(res, R - L + 1)
                curr_sum -= nums[L]
                L = L + 1
            
            R = R + 1

        if res == ( len(nums) + 1):
            return 0
        else:
            return res
        
