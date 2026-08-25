# This is a problem well suited for BFS

# Let's anyway use DFS an exercise
# DFS for every cell might be a solution
# Indeed a solution where you start dfs and store the minimum length to reach a trasure is
# TC : O( (mn) ^ 2 ), you need to do this for every cell
# SC : O( (mn) ). 


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        n, m = len(grid), len(grid[0])
        INF = 2 ** 31 - 1

        def dfs(r, c, visited):

            # Invalid states
            # discard already visited path down a state
            if (
                r < 0 or r >= n
                or c < 0 or c >= m
                or grid[r][c] == -1
                or (r, c) in visited
            ):
                return INF

            # Trasure found
            if grid[r][c] == 0:
                return 0

            # I need a way to know my path
            visited.add( (r, c) )

            down = dfs(r + 1, c, visited)
            up = dfs(r - 1, c, visited)
            right = dfs(r, c + 1, visited)
            left = dfs(r, c - 1, visited)

            visited.remove( (r, c) )

            return 1 + min ( down, up, right, left )

        for r in range(n):
            for c in range(m):

                if grid[r][c] == INF:
                    d = dfs(r, c, set())
                    
                    if d != INF:
                        grid[r][c] = d

