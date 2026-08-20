class Solution:
    def isValid(self, s: str) -> bool:

        # idea :
        # if a char is an open bracket --> ok
        # but we need to keep track of the last open bracket
        # if a closet bracket appears, it should match the last open bracket
        # if closed bracket and last open bracket matches --> ok
        # if not return False
        # a stack is perfectly fine for this problem
        # keep in the stk the last open bracket you saw
        # if a closet bracket appears and does not match --> return False
        # else --> pop the last bracket

        if not s:
            return True

        if len(s) == 1:
            return False

        d = { ")" : "(", "]" : "[", "}" : "{"} 
        stk = []

        for char in s :

            if char in d.values() :
                stk.append(char)  

            if char in d.keys()  :

                if stk and d[char] == stk[-1] :
                    stk.pop()
                else :
                    return False
       
        
                   
        if len(stk) == 0:
            return True
        else:
            return False    


          
