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
# It is forbidden to go backward, otherwise you would see a dfs(i-1).
# Think about this in the following way
# each solution creates [nums[i1], nums[i2], nums[i3], ... ] such that 
# i1 <= i2 <= i3 and so on

# There is another constraint right now
# " Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations."
# 

# The only way to skip duplicate is to sort
# It may take O ( n log(n) ) but it will get the job done
# By sorting we can skip dupilcates as we did in previous leetcode problems
# dfs is deterministic so with the same number it will generate the same outcome
# same root same outcome
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []
        candidates.sort()

        # i and total should be 0
        def dfs(i: int, total: int):

            # Valid subset
            if total == target:
                res.append(subset.copy())
                return
            
            elif total > target:
                return
            
            for j in range(i, len(candidates)):

                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                # now this is the first time we see canidates[j]
                subset.append(candidates[j])

                dfs(j + 1, total + candidates[j])

                subset.pop()

        dfs(0, 0)

        return res
            





    
        