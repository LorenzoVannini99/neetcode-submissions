# Idea :
# N = board_length
# Instead of 3 checks and 3 for loops
# Let's try to optimize the code
# Checking by brute force if a number, for each row and for each col
# contains a duplicate is expensive
# in that case complexity is quadratic for each row and for each col
# using a set simplify the code and the time complexity
# Use a list of sets
# Create one row_list_sets for N sets
# Create one col_list_sets for N sets
# for each loop of rows and cols use that set as the unique hashmap
# iterate through the set list each time a col or row as reached N - 1
# TC : O(N^2)
# SC : O(N)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        N = 9

        if not board :
            return None

        rows_list_set = [ set() for r in range(N) ]
        cols_list_set = [ set() for c in range(N) ]

        for r in range(N):
            for c in range(N):
                val_r = board[r][c]
                val_c = board[c][r]

                if val_r != ".":
                    if val_r not in rows_list_set[r]:
                        rows_list_set[r].add(val_r)
                    else:
                        return False    

                if val_c != ".":
                    if val_c not in cols_list_set[r]:
                        cols_list_set[r].add(val_c)
                    else:
                        return False                  

        # Checking centers
        C = []
        for x in range(1, N, 3):
            for y in range(1, N, 3):
                C.append( (x, y) )

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















