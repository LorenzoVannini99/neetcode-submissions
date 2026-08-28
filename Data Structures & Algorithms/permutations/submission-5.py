"""
# BackTrack solution

Given an array we want to return a permutation.
In a permutation the length is fixed, so len(element) == n == len(nums).

Now at each step, when you pick a number we must choose among n - 1 number, integers are different and distinct.

It each step we say, have we explored this path? meaning, have we choose this number or not?
It is not a binary tree like in subset, for each level i have : n choice, n - 1 choices,.. and so on.

At each step, have we picked the number or not?

sol = [] starts empty
consider all number
can I use nums[0]?
if yes
sol.append(nums[0])
can I use nums[1]?
if yes
sol.append(nums[1])
...
and so on.

Once it is completed (len(res) == n ), backtracks.

# EXAMPLE :
[1], [1,2], [1,2,3]--> copy sol
[1, 2] --> return None
[1, 3], [1, 3, 2]--> copy sol
..


"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res, sol = [], []

        def backtrack():

            if len(sol) == n:
                res.append(sol.copy())
                return
            
            for number in nums:
                if number not in sol:
                    
                    # use unused number
                    sol.append(number)

                    # backtrack
                    backtrack()

                    # undo the number
                    sol.pop()


        backtrack()

        return res


        