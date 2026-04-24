from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):

            if not 0 <= i < m or not 0 <= j < n or grid[i][j] == '0':
                return 
            else:
                grid[i][j] = '0'
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)

            
        I = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    I = I + 1
                    dfs(i,j)
        
        return I