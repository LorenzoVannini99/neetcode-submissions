import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Optimal solution
        n = len(position)

        x_non_sorted = [ (pos, speed) for pos, speed in zip(position, speed) ]
        
        # x = [ (p_{n}, v_{n}), (p_{n-1}, v_{n-1}), ... ]
        x = sorted( x_non_sorted, key = lambda s: s[0], reverse = True)
        print(x)
        
        stk = []

        T = [ (target - p)/ v  for p,v in x]
        print(T)
        
        res = 1  

        for t in T:
            if not stk:
                stk.append(t)

            else :
                if t > stk[-1]:
                    res = res + 1
                    stk.append(t)
        
        return res




        

         
       
    