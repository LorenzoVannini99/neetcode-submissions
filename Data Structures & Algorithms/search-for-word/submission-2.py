"""
DFS solution

A 2D grid can be viewed as a graph, where we find a valid path. This is the goal. Is there a valid path inside the grid?

Loop in the grid until you see the first letter, so loop until board[r][c] == word[0].
If it cannot be found return False.

If word is in the cell, start dfs from every possible 4 directions, up down right left.
The subtlety is to mark already visited cell avoiding double counting. 

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n, m = len(board), len(board[0])
        L = len(word)
        Visited = set()

        def dfs(r, c, i):

            # We matched the whole word
            if i == L:
                return True

            # Invalid cell
            if (
                r < 0 or r >= n or
                c < 0 or c >= m or
                (r, c) in Visited or
                board[r][c] != word[i]
            ):
                return False

            # Mark current cell as part of this path
            Visited.add((r, c))

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True

            # Backtrack
            Visited.remove((r, c))

            return False

        for r in range(n):
            for c in range(m):
                if dfs(r, c, 0):
                    return True

        return False
        
        