class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len ( heights )

        if n == 0 or n == 1 :
            return 0        
        
        l = 0
        r = n - 1
        max_area = 0

        while l < r :

            area = min(heights[l],heights[r]) * ( r - l )  
            max_area = max ( max_area , area)

            if heights[l] < heights[r] :
                l = l + 1
            else :
                r = r - 1

        return max_area
        