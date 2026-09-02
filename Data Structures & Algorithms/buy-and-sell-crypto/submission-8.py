"""
Idea :

max_profit = min_j = 1,...,i+j = n {sell[i + j] - buy[i] }

We have two indices so brute force leads to $O(n^2)$ solution. 
It works well but is not optimal.

You may even try to sort the prices but you need a way to keep the real index, and the sol is $O(nlogn)$

There exist a linear solution.
The idea is to use a sliding window approach.

Start = prices[index]
end = prices[index + i], and just move i

While the window is valid update max profit as max(max_profit, end - start).

If at some point prices[index + i] < Start, it means that I need to move my window.
Since I have already check for the maximum profit in the previous window.
If a greater profit exist it should be in that window.

Think about it, let's say 

[1,2,1,1,0,...]

start = 0
end = 4

valid window = [s, e]

so the max profit here is 1

when end = 5 and prices[end] = 0, from that point onward, if a max profit exists,
it should start from 0, the worst that can happen is that they stay at 0.

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #edge cases
        if (
            not prices or 
            len(prices) == 1 or 
            ( len(prices) == 2 and prices[0] >= prices[1]) 
            ):
            return 0

        start = prices[0]
        max_profit = 0

        for price in prices[1:]:

            max_profit = max(max_profit, price - start)

            if price < start:
                start = price



        return max_profit







        