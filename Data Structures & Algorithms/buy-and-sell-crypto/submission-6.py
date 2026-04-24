class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Idea :
        # Keep track of the minimum price seen so far
        # for a generic price p, if p < min price we update min price
        # else --> we can profit, if the profit is > than max profit 
        # we update max_profit

        if not prices :
            return 0
        
        min_price = prices[0]
        profit = 0

        for p in prices[1:] :

            if p < min_price :
                # no gain here
                min_price = p
            
            else :
                profit = max ( profit, p - min_price )

        return profit


 

        