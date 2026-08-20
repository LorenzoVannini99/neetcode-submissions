class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        t = temperatures
        n = len(t)
        stk = []
        r = [0] * n

        if n == 0 :
            return []

        stk = [ (0, t[0]) ]

        for i in range(1, n):
            while stk and t[i] > stk[-1][1]:
                r[stk[-1][0]] = i - stk[-1][0]
                stk.pop()
            
            stk.append( (i, t[i]) )
                
        return r