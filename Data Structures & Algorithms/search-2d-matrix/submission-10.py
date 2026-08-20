class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        

        # brute force solution
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
        
        return False
    
    # TC : O(n*m)
    # SC : O(1)
        

