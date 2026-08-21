# Visual Idea :

#                        backtrack(perm=[], pick=[F, F, F])
#                       /               |               \
#                Choose 1            Choose 2          Choose 3
#                /                      |                      \
#  perm=[1], pick=[T, F, F]   perm=[2], pick=[F, T, F]   perm=[3], pick=[F, F, T]
#      /           \              /           \              /           \
#  Choose 2     Choose 3      Choose 1     Choose 3      Choose 1     Choose 2
#    |             |             |             |             |             |
# [1,2,3]       [1,3,2]       [2,1,3]       [2,3,1]       [3,1,2]       [3,2,1]

# Starting from 1, I want 1 ---> 2 ---> 3
# 1 ---> 3 ---> 2
# I want to do ALL possible choices for each number
# goal: choose any number that has not been selected

# Termination is that is len(subset) == n
# Why?
# Because a permutation is complete when it contains all numbers.

# The question is : Which elements have I already used in the current permutation?
# At position 0, you can choose any element from nums.
# At position 1, you can choose any element except the one chosen for position 0.
# You continue until all elements are used (len(perm) == len(nums)).

# We need to store a list of picked elements called picked
# A simple list of booleans
# T T T F F F F F.. and so on

# TC : for each node you do n-1 permutations, so it is O(n * n!)
# SC : O(n * n!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs([], nums, [False] * len(nums))
        return self.res

    def dfs(self, perm: List[int], nums: List[int], picked: List[bool]):

        # Permutaion list is full, append to results
        if len(perm) == len(nums):
            self.res.append(perm.copy())
            return

        # Cycle until every number has been visited
        # Remember : In oyhton when a function reaches the end of its block
        # it returns None implicitly
        for i in range(len(nums)):
            if not picked[i]:
                perm.append(nums[i])
                picked[i] = True
                self.dfs(perm, nums, picked)

                perm.pop()
                picked[i] = False
