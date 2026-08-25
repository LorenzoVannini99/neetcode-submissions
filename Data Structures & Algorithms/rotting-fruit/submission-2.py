# Idea:
# BFS is a simple but effective solution
# Again we are looking for a problem where rotten fruits expands at a distance 1
# So clearly every freshfruit in the rotten square becomes rotten
# ( the rotten range from a fruit is a a square that takes the up right down or left squares )
# naturally bfs arises as the solution

# When do I stop?
# Well we stop where the number of fresh fruits = 0 
# the number of fresh fruits does not change after an iteration
# So we should keep track of it

# We might have mutiple rotten fruits so we can starts from there and expands outwardly
# so BFS with mutiple starting nodes is the natural solution

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # edge cases
        if not grid:
            return -1

        n, m = len(grid), len(grid[0])
        q = deque()
        step = 0

        fresh, rotten = 0, 0

        # TC : O(nm)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1

                elif grid[r][c] == 2:
                    q.append( (r, c) )
                    rotten += 1
        
        # edge cases
        if fresh == 0:
            return 0
        elif rotten == 0:
            return -1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while fresh > 0:

            old_fresh = fresh

            for _ in range( len(q) ):

                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if( 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1): 

                        grid[nr][nc] = 2
                        q.append( (nr, nc) )
                        fresh -= 1

            step += 1

            if fresh == old_fresh :
                return -1   


        return step
        


