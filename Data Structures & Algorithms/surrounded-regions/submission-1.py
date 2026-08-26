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
                    

  
















        