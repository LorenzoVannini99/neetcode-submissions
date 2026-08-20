class Solution:
    def isValid(self, s: str) -> bool:

        if not s :
            return True
        elif len(s) == 1 :
            return False    
        
        d = { "}" : "{" , "]" : "[" , ")" : "(" }
        stk = []

        for char in s :
            if char in d.values() :
                stk.append(char)
            else :
                if stk and d[char] == stk[-1] :
                    stk.pop()
                else :
                    return False
             
        if not stk :
            return True
        else :
            return False    
          