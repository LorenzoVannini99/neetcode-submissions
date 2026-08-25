# This is a problem well suited for BFS

# DFS for every cell might be a solution
# Indeed a solution where you start dfs and store the minimum length to reach a trasure is
# TC : O( (mn) ^ 2 ), you need to do this for every cell
# SC : O( (mn)^2 ). 

# BFS, as the name suggests, is breadth first search
# Starting from a source 0, it spreads out evenily in all directions
# ( think about a tree traverse with BFS is very intuitive )
# Starting from all 0 cells in parallel, if every bfs algorithm spreads evenly
# at the same velocity
# the first cell hit by the waves is the closest to a treasure
# the -1 acts as an interference

# BFS from treasures
# let's find every solution one step away
# then 2 steps away and so on
# of course a visited set should be used

# Visual idea : 
"""

 Wave Step 0:     Wave Step 1:         Wave Step 2:
  0   .   0        0 ~ 1 ~ 0            0 1 2 1 0
  .   .   .   -->  ~ 1 ~ 1 ~    -->     1 1 2 1 1
  .   .   .        ~ ~ ~ ~ ~            2 2 2 2 2

"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        n, m = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        # find zeros/treasures
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    queue.append( [r, c] )
                    visited.add( (r, c) )

        dist = 0
        directions = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

        while queue:

            for _ in range(len(queue)):

                r, c = queue.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < n and
                        0 <= nc < m and
                        grid[nr][nc] != -1 and
                        (nr, nc) not in visited
                    ):

                        visited.add( (nr, nc) )
                        queue.append( (nr, nc) )

            dist += 1
        



