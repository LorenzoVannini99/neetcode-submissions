class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        # optimal solution: unfolding
        # i need to map the index into row,col
        # index = 0 --> (0,0)
        # index = m --> (1,0)
        # index = m + 1 --> (1, 1)
        # index = index --> (index // m, index % m )

        n, m = len(matrix), len(matrix[0])

        l, r = 0, n*m - 1
        
        while l <= r:

            mid = ( l + r ) // 2

            row = mid // m
            col = mid % m

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                l = mid + 1
            
            else :
                r = mid - 1


        return False










        
        # TC : 
        # SC : 

        

