class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Idea :
        # We need an exhaustive search
        # backtracking is the solution but how to implement it ?
        # Let's think about what does it mean to have a combination sum
        # It means that given a number, you can do 3 things
        # do nothing
        # re sample that number
        # switch to another number
        # The constraint is : is the current sum less or equal than the target
        # example target = 20
        # curr number is 5
        # subset is [5, 5] 
        # is sum(subset) + curr < target ?
        # if yes use it and update subset
        # next numbers is 9
        # is sum(subset) + nextnumber < target ?
        # if yes use it and update subset
        # if next number was 25
        # is sum(subset) + nextnumber < target ? NO do not down that path
        # is sum(subset) + nextnumber == target ? yes, append it to res
        # and so on

        # What backtracking really means

        # Backtracking is a systematic way to explore all possible combinations 
        # of decisions that could lead to a solution, 
        # but stop exploring early when we know a path can’t work.
        # It’s a controlled form of recursion:

        # At each step, you make a choice 
        # (e.g., include this number or not, pick this candidate or move on).
        # You go deeper (recursively) with that choice.

        # If at some point that choice leads to an invalid or complete solution, 
        # you either:
        # record it (if valid)
        # or backtrack (undo that choice and try something else)

        # So, the key loop is:
        # make a choice → explore → undo the choice (backtrack)

        res = []
        subset = []
        
        def dfs(i, summation) :

            if summation == target:
                res.append( subset.copy() )
                return 

            if i == len(nums) or summation > target :
                return    
            
            subset.append(nums[i])
            dfs(i, summation + nums[i] )
            subset.pop()
            
            dfs(i + 1, summation )
        

        dfs(0, 0)
        return res



