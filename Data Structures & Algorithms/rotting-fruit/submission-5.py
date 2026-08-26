"""
BFS is needed.
Why?
Well we need a way to spread evenly the rotten fruits.
So naturally I would not choose DFS.

BFS must be chosen in scenario where something needs to be spread evenly accorss the grid.
Despite this other solution can be used but BFS is the natural choice.

# How to implement this?
Use MULTIPLE SOURCE BFS, because the question asks specifically 

" Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1."

First map the grid to obtain rotten fruit position

Start from each rotten cell, spread in every possible direction,
visit the cell only if is valid and its value is == 1
otherwise just pass.

# What about edge cases ?
We do have edge cases.

We need a way to keep track of how many fresh fruits we have, if the number of fresh fruits does not change
or the number of fresh fruit is 0 return the needed step

In this case
Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

fresh fruit = 3 for more than one iteraion so just return -1

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        q = deque()
        step = 0
        fresh, rotten = 0, 0

        directions = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

        # TC : O(mn)
        # Initialize q with rotten fruits position
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten += 1
                    q.append( (r, c) )
        
        # edge cases
        if fresh == 0:
            return 0
        if rotten == 0:
            return -1

        while fresh > 0:

            old_fresh = fresh

            for _ in range(len(q)):

                r, c = q.popleft()

                for dr, dc in directions:
                    # check every possible 4 directions
                    nr, nc = r + dr, c + dc

                    # valid states
                    if ( 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 ) :
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append( (nr, nc) )

            if fresh == old_fresh:
                return -1      
            step += 1

        return step














        