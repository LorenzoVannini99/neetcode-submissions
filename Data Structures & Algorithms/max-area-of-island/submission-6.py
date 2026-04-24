class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        
        A = 0
 
        def dfs(i,j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0

                c1 = dfs(i+1,j)
                c2 = dfs(i-1,j)
                c3 = dfs(i,j+1)
                c4 = dfs(i,j-1)

                return 1 + (c1+c2+c3+c4)

                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    A = max ( area , A)

        
        return A