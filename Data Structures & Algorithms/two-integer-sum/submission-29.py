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
# Just call res = target - number 
# Create an hashmap = h
# h[value] = i
# Why? Because I am saying "If you ever needed the number value, is at index i"
# If the residual is in the hasmap, if res in hashmap it's True
# the answer is result = [ h[res], current_index ]
# The hashmap is just a fast way to retrieve the index given the value
# Example : nums = [4,5,6], target = 10
# Step 1: number=4, complement=6
#        Is 6 in hashmap? No.
#        Store h[4] = 0      ← storing the NUMBER, not the complement

# Step 2: number=5, complement=5
#        Is 5 in hashmap? No.
#        Store h[5] = 1
#
# Step 3: number=6, complement=4
#        Is 4 in hashmap? YES ✅
#        Return [h[4], 2] = [0, 2]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for index, number in enumerate(nums):
            res = target - number

            if res in hashmap:
                return [hashmap[res], index]
            hashmap[number] = index


# TC : O(n)
# SC : O(n)