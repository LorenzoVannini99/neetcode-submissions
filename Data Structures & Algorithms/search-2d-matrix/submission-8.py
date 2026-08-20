class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len ( matrix )
        n = len ( matrix[0] )

        if m == n == 1 :
            if target == matrix[0][0] :
                return True
            else :
                return False
        
        l = 0
        r = m*n - 1

        while l <= r :

            mid = ( l + r) // 2

            row = mid // n 
            col = mid % n

            val = matrix[row][col]

            if val == target :
                return True
            elif val < target :
                l = mid + 1
            else :
                r = mid - 1        
        
        return False





        
