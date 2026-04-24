class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Optimal solution
        # Sliding window problem
        # You have 2 pointer , one is buy and one is sell
        # As long as the window is valid update gain = max(gain, prices[sell] - prices[buy])
        # How do we update?
        # gain = prices[sell] - prices[buy]
        # how do you maximize gain? minimizing prices[buy] or maximizing prices[sell]
        
        min_price = 100000000000
        max_price = 0
        max_gain = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                pass
            
            max_gain = max ( max_gain, prices[i] - min_price)


        return max_gain
            








        