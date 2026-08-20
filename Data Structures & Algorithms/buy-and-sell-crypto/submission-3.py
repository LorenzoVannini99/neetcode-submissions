class Solution:
    def maxProfit(self, prices: List[int]) -> int:
 
        min_value = prices[0]
        max_gain = 0

        for price in prices :
            
            if price < min_value :
                min_value = price 
            else :
                max_gain = max ( max_gain , price - min_value)

        return max_gain

        