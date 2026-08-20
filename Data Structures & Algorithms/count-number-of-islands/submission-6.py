# DFS solution
# Why DFS? well we need to traverse a graph so naturally
# dfs or bfs arise
# They have the same TC and SC so it's irrelevant in this case
#
# As far as I am concerned DFS feels more natural here
# traverse the "1"s near to you and avoid 0
# mark every 1 as 0 if visited
#
# Let's think about what to do in a single node level
#
# if it's "0" it is not relevant
# if it is "1" surely it will be at least one island so I = I + 1
# now to be connected it means that its neighboors are "1"
# is there a "1" down, left, up or right? 
# if yes, well it means we need to go down that path, 
# because other components might be "1".
# If there is a zero we might just ignore it
# This is the idea
# In order to avoid double counting we can just 
# set the previous 1 to 0
# if it is out of bound just pass
# "go as far as you see one up down right or left and set it to zero, if there is no other one left, find another island"
#
# VARIANT:
# if diagonal connections were considered just add dfs(i+-1, j+-1)
# and check 8 different subcells at most for each cell
#

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        def dfs(i, j):

            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return 
            else:
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)                

        I = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    I = I + 1
                    dfs(i, j)

        return I

# TC : O(nm)
# SC : O(nm), since running recursively something fills the stack





        