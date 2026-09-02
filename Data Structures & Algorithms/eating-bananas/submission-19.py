"""
Idea :

We have $p = [p_1,,,,p_n]$ where $p_i >= 0$ and an integer $h > 0$

The goal is to find $k>0$ such that $k = k_min \text{min hour rate to finish bananas}$

First define a function that given $k, p$ it gives you the estimated hours time

$$f(k, p) = H$$

if $k=1$ $f(k=1, p) = sum(p)$, of course if $h >= sum(p)$ return $k=1$.

if $k=max(p)$, $f(k=max(p), p) = len(p)$, so $h$ must be greater than piles's length.

k_min = 1
k_max = max(p)

Now we are interested in the minimum possible k such that f(k, p) <= h.

Just use Binary Search.
Why?

Beacuse f is a non increasing function with k, if k1 >= k2 f(k1) <= f(k2).

L = k_min = 1
R = k_max = max(p)

[L, R] contains the optimal element
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def f(k):
            H = sum ( [ math.ceil(p / k) for p in piles ] )
            return H

        # k_min = 1
        # k_max = max(p)
        L = 1
        R = max(piles)

        while L < R:

            m = (L + R) // 2

            if f(m) <= h:
                R = m
            else:
                L = m + 1

        return L





        