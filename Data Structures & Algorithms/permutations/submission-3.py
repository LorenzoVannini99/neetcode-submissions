# Length of each element list is fixed = n
# you must create each permutaions of length n fo each list
# list 1--> all permutations
# list2 --> all permutations...
# and so on
# SO it is going to be quite large
#
# TC : O( n! * n )
# SC : O( n! * n ) 
# 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        results = []
        per = []
        picked = [False] * n
        

        def dfs(per, nums, picked):

            if len(per) == n :
                results.append(per.copy())
                return
            
            for i in range(n):
                if not picked[i]:
                    per.append(nums[i])
                    picked[i] = True
                    dfs(per, nums, picked)

                    per.pop()
                    picked[i] = False

        dfs(per, nums, picked)

        return results