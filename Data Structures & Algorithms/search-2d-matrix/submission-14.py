class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        # Suboptimal solution
        n, m = len(matrix), len(matrix[0])
        
        r, row = 0, 0

        while r < n and matrix[r][0] <= target:
            row = r
            r = r + 1

        # Binary search on row
        target_vector = matrix[row]

        l = 0
        r = m - 1

        while l <= r :
            mid = ( l + r ) // 2
            
            if target_vector[mid] == target:
                return True

            elif target_vector[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1

        return False
        










    
    # TC : 
    # SC : 
        

