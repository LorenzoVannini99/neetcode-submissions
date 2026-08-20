# Same ideas as before
# for each number you may take or not take the same number or other number
# in this case the part where the leaf is not when we have reached index = n
# rather if the sum is greater than the target
# We must create a set of all distinct solution
# [2, 2, 5] is the same sol as [5, 2, 2]


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []

        def dfs(i):

            if sum(subset) == target:
                res.append(subset.copy())
                return

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
        