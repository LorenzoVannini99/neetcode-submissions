# Visual Idea :
# 1
# ├── take 1
# │   ├── take 2
# │   └── skip 2
# └── skip 1
#    ├── take 2
#    └── skip 2
# .... and so on
# for each node, take the node or do not
# so for each nod we have two choices
# 2 * 2 * .... = 2^n
# We must traverse the graph so it is going to be TC: O( 2^n * n )
# SC : O(n) since we are using dfs + choices

# How to create the code?

# dfs(index, subset) is the natural choice
# dfs(0, []) --> i am looking at the element 0 and my current subset is empty
# Take 1  -> dfs(1, [1])
# Skip 1  -> dfs(1, [])
# if we reach the last possible number which is len(nums), 
# in this case 3, we simply append it to results
# beacuse no other choice can be made
# we have reached a leaf

# If you use python, remember to use subset.copy()
# subset.copy() = a photograph of the subset at that moment.
# The problem is that in python everything is an object 
# so the name is a placeholder for the pointer to the real object
# use .copy() to avoide any type of problems

# Create two lists
# results ( output )
# subset

# if index == len(nums):
#   res.append(subset.copy())
#   return 

# 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []
        subset = []

        # dfs is the natural choice
        # The space of all subset can be seen as a tree
        def dfs(i):

            # leaf reached, no other choice can be made
            if i == len(nums): 
                results.append( subset.copy() )
                return 

            # if leaf is not reached we have a root
            # first choice : take the number
            # update the subset and go to the next index
            subset.append(nums[i])
            dfs(i+1)

            # second choice do not take the number
            # so pop the subset
            subset.pop()
            dfs(i+1)

        dfs(0)

        return results



