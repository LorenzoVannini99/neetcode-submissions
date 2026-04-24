class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Optimal solution
        t = temperatures
        n = len(t)
        res = [0] * n
        stk = []

        for index, value in enumerate ( t ):

            if not stk:
                stk.append( [value, index] )

            else:

                while stk and value > stk[-1][0]:
                    last_index = stk[-1][1]
                    res [ last_index ] = index - last_index
                    stk.pop()
                
                stk.append( [value, index] )
                    
        return res








        








        