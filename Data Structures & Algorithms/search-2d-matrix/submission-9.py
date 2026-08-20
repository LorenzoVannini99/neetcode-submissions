class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #
        # m = rows
        # n = columns
        # Idea :
        # From text: "Can you write a solution that runs in O(log(m * n)) time?"
        # simply unroll the matrix into a single column vector
        # the vector has m*n component
        # create an algorithm that maps the position in the vector with matrix[r][c]
        # index = 0 --> (0,0)
        # index = 1 --> (?,?)
        # index = i --> (?,?)
        # 
        # If matrix = [[1,2,4,8],[10,11,12,13]], m = 2, n = 4
        # v = [1,2,4,8,10,11,12,13]
        # if index is 4 (pos = 5) i am at the second row
        # index is 5 (pos = 6) i am STILL at the second row
        # row = index // n
        #
        # if index is 4 ( pos = 5 ) i am in the col = 0
        # if index is 5 ( pos = 6 ) i am in the col = 1
        # if index is 7 ( pos = 8 ) i am in the col = 3
        # if index is 8 ( pos = 9 ) i am in the col = 0
        # col = index % n 
        #

        m = len(matrix)
        n = len(matrix[0])
         
        l = 0
        r = m*n - 1

        while l <= r:

            index = ( l + r ) // 2
            
            row = index // n
            col = index % n
            
            if matrix[row][col] > target :
                r = index - 1

            elif matrix[row][col] < target:
                l = index + 1

            else :
                return True         
                
        return False
        
