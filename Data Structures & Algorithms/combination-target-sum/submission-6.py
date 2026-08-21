# Visual idea : 

#                nums[i]
#              /         \
#           TAKE         DON'T TAKE
#            /             \
#       dfs(i)            dfs(i+1)

# Same ideas as before
# for each number you may take or not take the same number or other number
# in this case the part where the leaf is not only when we have reached index = n
# but if the sum is greater than the target and the index = n

# We must create a set of all distinct solution
# [2, 2, 5] is the same sol as [5, 2, 2]
# Luckily for us this is indeed the case
# once you find a combination that works
# no other same pairs of number can be used to create the same target
# WHY?
# Well, once an index is taken, 
# it can be taken an infinite amount of time as long as the subset is valid
# once validation falls, the index is moved and we go to the next index
# It is forbidden to go backward, otherwise you would see a dfs(i-1).
# Think about this in the following way
# each solution creates [nums[i1], nums[i2], nums[i3], ... ] such that 
# i1 <= i2 <= i3 and so on
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []

        def dfs(i):
            
            # Valid subset
            if sum(subset) == target:
                res.append(subset.copy())
                return

            # Not valid
            elif i >= len(nums) or sum(subset) > target:
                return 

            else:

                # I can reuse the same number again, so same index
                subset.append(nums[i])
                dfs(i)
                subset.pop()

                dfs(i+1)

        dfs(0)

        return res



# TC = ?
# You visit every node so at least is n
# for every node you may take the same node as long is less than target
# Let's call the target T
# if m= min(nums)
# The max length of the subset is T/m
# then the sum of subset is computed and subset.copy() is computed
# O ( 2^ T/m + n  + n ) = O( 2 ^ T/m )

# SC = ?
# SC is the depth of dfs, so O( 2^ T/m )
        