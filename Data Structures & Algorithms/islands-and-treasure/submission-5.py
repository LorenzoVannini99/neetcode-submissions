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

# We can skip visited set
# I must change the grid IN PLACE
# so starting from the trasures, where grid[r][c] == 0
# I move in every 4 possible direction where state is valid and grid[r][c] == INF
# If I can move in a valid cell the value of that grid is value of previous grid + 1
# Since i am only moving in INF cells, i am guaranteed that i will not re visit same state
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        n, m = len(grid), len(grid[0])
        q = deque()
        INF = 2 ** 31 - 1 # float("inf")

        # Find treasures in O(nm) time
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    q.append( (r, c) )

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q :

            r, c = q.popleft()

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if ( 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == INF ) :
                    q.append( [new_r, new_c] )
                    grid[new_r][new_c] = grid[r][c] + 1






        