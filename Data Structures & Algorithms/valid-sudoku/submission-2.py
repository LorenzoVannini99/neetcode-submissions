class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Define centers and directions
        centers = []

        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                centers.append([i,j])
        
        directions = []

        for i in [-1,0,1]:
            for j in [-1,0,1]:
                directions.append([i,j])
        
        # define dimensions
        n = len(board)
        m = len(board[0])
        

        # Centers
        for c in centers:
            S = set()
            for d in directions:
                element = board[c[0] + d[0]][c[1] + d[1]]
                if element != "." :
                    if element not in S:
                        S.add(element)
                    else :
                        return False    


        for i in range(n):
            S = set()
            for j in range(m):
                element = board[i][j]
                if element != "." :
                    if element not in S:
                        S.add(element)
                    else :
                        return False 

        
                
        for j in range(n):
            S = set()
            for i in range(m):
                element = board[i][j]
                if element != "." :
                    if element not in S:
                        S.add(element)
                    else :
                        return False 

        
        return True

        


    