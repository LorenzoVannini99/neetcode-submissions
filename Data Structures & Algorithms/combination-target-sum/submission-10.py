class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        results = []
        subset =  []

        def dfs(i : int):

            if sum(subset) == target :
                results.append(subset.copy())
                return 
            
            elif i == len(nums) or sum(subset) > target:
                return
            
            else :

                subset.append(nums[i])
                dfs(i)

                subset.pop()
                dfs(i+1)

        dfs(0)

        return results