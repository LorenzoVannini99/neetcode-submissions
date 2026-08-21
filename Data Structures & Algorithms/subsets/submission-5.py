# I have a tree 
#    []
#   /  \
#  1    not 1
#.. 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []
        subset =  []

        def dfs(i : int):

            if i == len(nums):
                results.append(subset.copy()) # TC : O(k) where k is the subset length
                return 

            subset.append(nums[i]) # select the number ; TC : O(1)
            dfs(i +  1) # branches selected number

            subset.pop() # pop last number ; TC : O(1)
            dfs(i + 1) # branches no selection

        dfs(0)

        return results



        