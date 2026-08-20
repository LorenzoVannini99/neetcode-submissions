class Solution:
    def isValid(self, s: str) -> bool:

        if not s :
            return True
        elif len(s) == 1 :
            return False    
        
        d = { "}" : "{" , "]" : "[" , ")" : "(" }
        stk = []
       
        for char in s :
            if char not in d.keys() :
                stk.append ( char )
            else :
                if not stk or stk.pop() != d[char] :
                    return False
                 
        if not stk :
            return True
        else :
            return False    