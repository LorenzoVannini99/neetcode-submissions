class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        results = []
        subset =  []

        def dfs(i : int, curr_sum : int):

            if curr_sum == target :
                results.append(subset.copy())
                return 
            
            elif i == len(nums) or curr_sum > target:
                return
            
            else :
                subset.append(nums[i])
                dfs(i, sum(subset))

                subset.pop()
                dfs(i+1, sum(subset))

        dfs(0, 0)

        return results