# This is a std graph problem:
# The idea is simple :
# traverse all the graph and look for connected components

# This is not so much different from the word search problem from backtracking
# look all near components
# to avoid double counting backtracks and put "0" instead of "1" is a one is found
# look in every 4 direction
# You want to keep track of the number of islands so far
# so time and space complexity will be in the order of O(nm)

# First create a dfs function that tells you if from a point
# grid[r][c] an island is there or not
# if yes remember to set all the ones you found to 0 avoid double counting
# then just sum the global number of islands

# The idea is to eliminate all near "1" once a single 1 is found
# repeat the idea for all "1"s

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n, m = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):

            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == "0":
                return 
            
            else :

                grid[r][c] = "0"

                dfs(r + 1, c) 
                dfs(r - 1, c) 
                dfs(r, c + 1) 
                dfs(r, c - 1) 


        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res   



        