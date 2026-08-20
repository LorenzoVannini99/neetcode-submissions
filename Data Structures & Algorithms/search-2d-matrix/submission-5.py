class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len ( matrix )
        n = len ( matrix[0] )

        if m == n == 1 :
            if target == matrix[0][0] :
                return True
            else :
                return False
        
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        
        i = m - 1
        
        while target < matrix[ i ][0]  and i >= 0:
            i = i - 1 
        
        v = matrix[i]
        
        l = 0
        r = n - 1

        while l <= r :
            mid = (l + r) // 2
            if v[mid] == target :
                return True
            elif v[mid] > target :
                r = mid - 1
            else :
                l = mid + 1
        
        return False




        
