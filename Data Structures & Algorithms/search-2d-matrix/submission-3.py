class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        j = m - 1
        
        if target > matrix[m - 1][n - 1] or target < matrix[0][0] :
            return False

        while matrix[j][0] > target and j > 0 :
            j = j - 1
        

        row_target = matrix[j]
        l = 0    
        r = n - 1 

        while l <= r :
            index = ( l + r ) // 2
            
            if target > row_target [index] : 
                l = index + 1

            elif target < row_target [index] :
                r = index - 1 

            elif target == row_target[index] :
                return True

        return False
        