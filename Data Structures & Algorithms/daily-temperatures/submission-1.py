class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        t = temperatures 
        n = len ( t )

        if n == 0 or n == 1 :
            return [0]
        
        stk = []
        res = [0] * n
        i = 1

        for index,value in enumerate ( t ) :

            if not stk :
                stk.append ( [value,index] )
            else :
                while stk and t[ index ] > stk[-1][0] :
                    last_element = stk.pop()
                    res[last_element[1]] = index - last_element[1]
                     
                stk.append ( [value,index])


        return res


        