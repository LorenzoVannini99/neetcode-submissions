# Visual Idea :
#    1
#   /  \
#  2    3
#    3
#   /  \
#  2    1
# ....

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

# termination is that is len(subset) == n
# Why?
# Because a permutation is complete when it contains all numbers.

# The question is : Which elements have I already used in the current permutation?
# At position 0, you can choose any element from nums.
# At position 1, you can choose any element except the one chosen for position 0.
# You continue until all elements are used (len(perm) == len(nums)).


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        # pick tracks whether nums[i] is currently inside `perm`
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        # Base Case: All slots filled, we found a valid permutation
        if len(perm) == len(nums):
            self.res.append(perm[:])  # Make a copy of perm to preserve the snapshot
            return

        for i in range(len(nums)):
            if not pick[i]:  # Element nums[i] is available
                # 1. CHOOSE
                perm.append(nums[i])
                pick[i] = True

                # 2. EXPLORE
                self.backtrack(perm, nums, pick)

                # 3. UNCHOOSE (Backtrack to explore other choices)
                perm.pop()
                pick[i] = False
        