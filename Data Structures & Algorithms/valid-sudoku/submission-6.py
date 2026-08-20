# Idea :
# Checking by brute force if a number, for each row and for each col
# contains a duplicate is expensive
# in that case complexity is quadratic for each row and for each col
# using a set simplify the code and the time complexity
# to check 3 x 3 sub boxes, grid validation we can use the centers
# maybe does not scale well, but 
# C = { (1,1), (1,4), (1,7), (1,1), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7) }
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        Size = 9

        if not board :
            return None

        # Rows check
        for r in range(Size):
            row_set = set()

            for c in range(Size):
                if board[r][c] != ".":
                    if board[r][c] not in row_set :
                        row_set.add(board[r][c])
                    else:
                        return False

        # Columns check
        for c in range(Size):
            col_set = set()
            for r in range(Size):
                if board[r][c] != ".":
                    if board[r][c] not in col_set :
                        col_set.add(board[r][c])
                    else:
                        return False

        # centers check
        C = { (1,1), (1,4), (1,7), (1,1), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7) }
        directions = [-1 , 0 , 1]

        for centers in C:

            r = centers[0]
            c = centers[1]
            centers_set = set()

            for dx in directions:
                for dy in directions:
                    if board[r + dx][c + dy] != ".":
                        if board[r + dx][c + dy] not in centers_set :
                            centers_set.add(board[r + dx][c + dy])
                        else:
                            return False

        return True



















