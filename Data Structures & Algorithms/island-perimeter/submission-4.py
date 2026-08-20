
# Island Perimeter Solution
# Iterative 
# The perimeter of one single "1" island is 4
# if an island is close to 4 ones is perimeters is 0
# perimeter(grid[i][j]) = 4 - neighboors 
# 
# Simple solution 
# TC : O(nm)
# SC : O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def is_land(i, j):

            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            else:
                return 1

        p = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    
                    neighbors = (
                    is_land(i + 1, j) +
                    is_land(i - 1, j) +
                    is_land(i, j + 1) +
                    is_land(i, j - 1)
                    )
                
                    p = p + 4 - neighbors

        return p



