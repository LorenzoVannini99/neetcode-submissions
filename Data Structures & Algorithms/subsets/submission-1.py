class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums :
            return 

        result = []
        current = []

        def dfs(i):
            if i == len( nums ) :
                result.append( current.copy() )
                return     
            
            current.append(nums[i])
            dfs(i + 1)

            current.pop()
            dfs(i + 1)

        dfs(0)

        return result    



   


        
        