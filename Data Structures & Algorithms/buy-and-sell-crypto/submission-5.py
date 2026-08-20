class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len ( prices )
        
        if n == 1 :
            return 0
        
        max_gain = 0
        
        minimum = prices[0]

        for r in range ( n ) :

            if prices[r] < minimum :
                minimum = prices[r]
                
            
            max_gain = max ( max_gain , prices[r] - minimum)


        return max_gain    



 

        