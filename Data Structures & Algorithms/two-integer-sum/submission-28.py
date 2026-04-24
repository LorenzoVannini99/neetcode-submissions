# Optimal Solution :
# The solution is guaranteed to exists
# There must be 2 indices i,j st nums[i] + nums[j] == target
# Just use a hashmap
# a hashmap is a great way to solve this because it's a fast lookup table
# It costs on average O(1) so it's pretty fast
# How to use it ?
# Well you have to think about a way to create a smart key value couple
# Work with residuals
# Let's say as I said before that nums[i] + nums[j] == target, where i and j can go from 1 to n
# Let's say I start from the index k and compare it with index j
# nums[k] + nums[j] != target
# they do not add up to target
# but if i find an index such that target - nums[index] = nums[k] I found the numbers
# Just call res = target - number 
# Create an hashmap = h
# h[value] = index
# or
# h[res] = index
# In words : 
# "If you ever find a number such that is in the hashmap the result is [h[number], current_index]"
# Now if I every stumbled upon res in hashmap I have found the two numbers
# Example :
# nums = [4,5,6], target = 10
# h[10-4] = h[6] = 0
# h[5] = 1
# 6 is in  the hashmap
# so result = [h[6], current_index] = [0, 2]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums or len(nums) == 1:
            return
        
        hashmap = {}

        for index, number in enumerate(nums):
            res = target - number

            if res in hashmap:
                return [hashmap[res], index]
            hashmap[number] = index





# TC : O(nlog(n))
# SC : O(n)