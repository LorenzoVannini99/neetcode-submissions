class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if not temperatures :
            return [0]
        elif len(temperatures) == 1 :
            return [0]
        
        t = temperatures
        n = len( t )
        stk = []
        res = [0] * n

        for index,value in enumerate ( t )  :
            if stk :
                while stk and value > stk[-1][1] :
                    popped = stk.pop()
                    res [ popped[0] ] = index - popped[0] 

                stk.append([index,value])

            if not stk :
                stk.append([index,value])  

        return res
            
            





        