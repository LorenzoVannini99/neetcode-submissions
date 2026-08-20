# Hashmap sol
# n = len(nums)
#
# Idea :
# if two indices are guaranteed to exist
# nums[i] + nums[j] == target
# work with residuals
# nums = [ nums[0], nums[1],..., nums[ len(nums) - 1 ]]
# let's say nums[0] + nums[ len(nums) - 1 ] == target
# Brute force solution check every possible couples TC : O(n^2), SC:O(1)
# Use a hashmap to immediately know if the residual is in the hashmap
# h = hashmap
# residual = target - nums[0]
# is residual in h? if not h[nums[0]] = 0
# if it is return[h[res], curr_index]
#
# In our case :
# h = hashmap
# residual = target - nums[0]
# is residual in h? 
# h[nums[0]] = 0
# ..
# residual = target - nums[ len(nums) - 1 ]
# residual == nums[0]
# if residual in h
# return [h[res], current index]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return 
        
        h = {}

        for index, value in enumerate ( nums ):
            res = target - value
            if res not in h:
                h[value] = index
            else :
                return [h[res], index]    

# TC : O(n)
# SC : O(n)