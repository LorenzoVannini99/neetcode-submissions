"""
The key observation is:

An "O" is surrounded if and only if its connected component
does NOT touch the border.

Therefore, instead of starting DFS from every "O" and checking
whether its component reaches the border, I can work backwards:

Start DFS from every "O" that is already on the border.

Why?

Any "O" connected to a border "O" cannot be surrounded.
Therefore, every "O" reached by these DFSs is SAFE and must remain "O".

So:

SAFE = all "O" cells connected to the border.

Then, after finding all SAFE cells, scan the entire board:

- If a cell is "O" and is in SAFE -> leave it unchanged.
- If a cell is "O" and is NOT in SAFE -> it is surrounded, so change it to "X".

# How to implement this?

1. Find every border "O".
2. Put them into SAFE.
3. Keep the original border cells in SAFE_LIST.
   I need a separate list because DFS will add more cells to SAFE,
   and I cannot iterate over a set while modifying it.
4. Run DFS from every cell in SAFE_LIST.
5. During DFS, only visit neighboring "O" cells that are not already SAFE.
6. Finally, scan the whole board and flip every "O" not in SAFE.

The central idea is:

    SAFE = { O cells connected to the border }

Therefore:

    O and not SAFE -> X
    O and SAFE     -> remain O

Complexity:

Time:  O(n * m)
Space: O(n * m)

because in the worst case DFS can visit every cell.

"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board :
            return []
        
        n, m = len(board), len(board[0])
        
        # create a SAFE set
        # create a SAFE list avoiding itearation problems
        SAFE = set()
        SAFE_LIST = []

        directions = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

        # find all the starting "O" in the board's edge
        for r in range(n):
            if board[r][0] == "O":
                SAFE.add( (r, 0) )
                SAFE_LIST.append( [r, 0] )

            if board[r][m - 1] == "O":
                SAFE.add( (r, m - 1) )
                SAFE_LIST.append( [r, m - 1] )

        for c in range(m):
            if board[0][c] == "O":
                SAFE.add( (0, c) )
                SAFE_LIST.append( [0, c] )

            if board[n - 1][c] == "O" :
                SAFE.add( (n - 1, c) )
                SAFE_LIST.append( [n - 1, c] )

        def dfs(r, c):

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 
                    0 <= nc < m and 
                    (nr, nc) not in SAFE and 
                    board[nr][nc] == "O" ):

                    SAFE.add( (nr, nc) )
                    dfs(nr, nc)

        # Find all safe "O"s
        for safe_r, safe_c in SAFE_LIST:
            dfs(safe_r, safe_c)          


        for r in range (n):
            for c in range(m):
                if board[r][c] == "O" and (r, c) not in SAFE:
                    board[r][c] = "X"
                    

  
















        