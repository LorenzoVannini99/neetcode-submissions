class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len ( board )
        m = len ( board [0] )

        centers = [[1,1] , [1,4] , [1,7] , [4,1] , [4,4] , [4,7], [7,1] , [7,4] , [7,7]]
        directions = [[0,0],[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

        for r in range ( n ) :
            seen_row = set()
            for c in range ( m ) :
                if board[r][c] != "." :
                    if board[r][c]  in seen_row:
                        return False
                    else :
                        seen_row.add(board[r][c])    
        

        for c in range ( m ) :
            seen_col = set()
            for r in range ( n ) :
                if board[r][c] != "." :
                    if board[r][c]  in seen_col:
                        return False
                    else :
                        seen_col.add(board[r][c])    
         
        for c in centers :
            seen_centers = set()
            for d in directions :
                val = board [ c[0] + d[0] ][c[1] + d[1]]
                if  val != "." : 
                    if val in seen_centers :
                        return False
                    else :
                        seen_centers.add(val)

            
        return True

            
