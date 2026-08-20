class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0 :
            if n > 0 :
                return 0
            else :
                return float('inf')    
            
        elif x > 0 :
            if n > 0 :
                c = 1
                for i in range(n):
                    c = c*x
                return c

            elif n < 0 :
                c = 1
                for i in range(-n):
                    c = c/x
                return c

            else :
                return 1 
        
        else :
            if n > 0 :
                c = 1
                for i in range(n):
                    c = c*x
                return c

            elif n < 0 :
                c = 1
                for i in range(-n):
                    c = c/x
                return c

            else :
                return 1 

