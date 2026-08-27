"""

First sol: 

This problem solves the opposite of happy number.

Given digits = [d0, d1, .., dm-1] where m = len(digits)

d = dm-1 * 10 ** 0 + dm-2 * 10 ** 1 + ... +  d0 * 10 ** (m-1)

n = d + 1

n = n0n1...nk-1

res = [n0, n1,..., nk-1]

while n > 0:
    res.append ( n % 10 )
    n = n // 10

res.reverse()

return res

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        d = 0
        m = len(digits)

        for i in range(m):

            digit_i = digits[i] * 10 ** (m - i - 1)

            d = d + digit_i

        n = d + 1
        res = deque()

        while n > 0:
            res.appendleft ( n % 10 )
            n = n // 10
        
        return list(res)