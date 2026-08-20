from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])

        def bfs(i,j):
            
            if  0 <= i < m and 0 <= j < n and grid[i][j] == '1':

                q = deque()
                q.append((i,j))

                while q :
                    i,j = q.popleft()
                    grid[i][j] = '0'

                    if 0 <= i + 1 < m and grid[i + 1][j] == '1':
                        q.append((i + 1,j)) 

                    if 0 <= i - 1 < m and grid[i - 1][j] == '1':
                        q.append((i - 1,j))

                    if 0 <= j + 1 < n and grid[i][j + 1] == '1':
                        q.append((i,j + 1)) 

                    if 0 <= j - 1 < n and grid[i][j - 1] == '1':
                        q.append((i,j - 1)) 



        I = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    I = I + 1
                    bfs(i,j)
        
        return I