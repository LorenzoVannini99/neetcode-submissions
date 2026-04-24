# Idea :
# N = board_length
# Instead of 3 checks and 3 for loops
# Let's try to optimize the code
# Checking by brute force if a number, for each row and for each col
# contains a duplicate is expensive
# in that case complexity is quadratic for each row and for each col
# using a set simplify the code and the time complexity
# Do everything in only one pass
# 9 sets for rows
# 9 sets for cols
# 9 sets for boxes
# for each pass we update the set
# We need a function to map a position (r, c) into a box
# 0,0 is first box; 0,1 and 1,0 is is first box; 2,3 is second box
# We need a function that if r = 4 for the first 3 columns i should return 4 as an index
# Standard Formulas for 2D array ; 
# index = row * width + col
# the idea is simple, box_index = ( r // 3 ) * 3 + ( c // 3 )
# TC : O(N^2)
# SC : O(N)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if not board :
            return True

        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        box_set = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_index = ( r // 3 ) * ( 3 ) + ( c // 3 ) 
                if val != ".":
                    if (val in row_set[r]) or (val in col_set[c]) or (val in box_set[box_index]) :
                        return False
                    else :
                        row_set[r].add(val)
                        col_set[c].add(val)
                        box_set[box_index].add(val)

        return True

        















