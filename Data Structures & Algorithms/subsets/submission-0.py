class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Whenever an exhaustive search it is called, 
        # that's when backtracking is useful
        # Given the a certain state s, we could have few actions or solutions
        # In this case : you start with no number . No number whatsoever. 
        # Nothing is a then you go to the first number. 
        # The first number can or cannot be chosen
        # i.e : [1, 2, 3]
        # Start with : []
        # to the left you might have [1] or []
        # your tree has now one root = []
        # and two children [] and [1]
        # from the left leaf to the right decide whetehr you choose or not that number
        # Now go to the second number : 2
        # from [], to the left --> do not choose. To the right --> choose the number
        # root = [] and leaves [] and [2].
        # root = [1] and leaves are [1] or [1,2]

        # Think about it
        # Each result should represent whether or not you did a certain action/choice 

        # root = [] --> leaves = [] or [3]

        # root = [2] --> leaves = [2] or [2, 3]

        # root = [1] --> leaves = [1] or [1, 3]

        # root = [1,2] --> leaves = [1,2] or [1,2,3]
        
        # Computationally, the recursive call is done with a dfs
        # The path that the computer would take is start with an empty list
        # then go in depth first, then undo.
        # It is called backtracking since the algorithm backtrackes, it goes back up.
        # dsf is an exhaustive search as we all know. 
        # This is a, computationally speaking, nightmare
        # TC : O(2^n * average length of subset ) = O( 2^n * n)
        
        # Each path gives a state. 
        # From a state we will recursively call the function
        # At each state ask : 
        # What can i do? Can i go to the left? Can i go to the right?
        # So each branch will create other 2 branches.
        # if an action is forbidden just prune the tree and store the results.

        # Ok How to do it ?

        # use res and sol such that, we update sol until i get a base case == leaf
        # after that the sol is back at res.
        # using sol.copy() to create a copy
        # subset is a reference of subset, it will be modified.
        # so pass subset.copy()

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) # We have reached a leaf
                return 
            
            # include nums[i], left decision
            subset.append(nums[i])
            dfs(i+1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i+1)
            
        
        dfs(0)
        return res


        
        