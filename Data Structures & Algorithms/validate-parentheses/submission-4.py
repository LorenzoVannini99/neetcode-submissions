class Solution:
    def isValid(self, s: str) -> bool:

        if not s :
            return True
        if len(s) == 1 :
            return False    
        
        d = {  "}" : "{" , "]":"[" , ")": "(" }

        stk = []

        for char in s :

            if char in d.values() :
                stk.append(char)

            else :
                if stk :
                    last_element = stk.pop()
                else :
                    return False

                if not d [ char ] == last_element :
                    return False 

        if len(stk) == 0 :
            return True
        else :
            return False            