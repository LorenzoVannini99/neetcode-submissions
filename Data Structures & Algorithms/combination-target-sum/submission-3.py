class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        current = []
        
        # i is the current index of nums

        def dfs(i, summation):

            if i >= len(nums) or summation > target :
                return

            if summation == target :
                result.append( current.copy() )
                return 

            current.append ( nums[i] )
            dfs(i, summation + nums[i] )
            current.pop()

            dfs( i + 1 , summation)

        dfs(0, 0)
        return result    







