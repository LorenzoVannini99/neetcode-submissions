# Idea :
# in this case stack are useful
# you want a data structure that let you prioritize the last element
# if s = ({}[])
# at each stage you want to prioritize the last open element
# The last element has priority over the previous one
# if a close bracket appears, it's important to check
# if it matches the open bracket
# use a dictionary to store correct close and open brackets
class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s :
            return True
        elif len(s) == 1:
            return False
        
        d = { "}" : "{", "]" : "[", ")" : "(" }
        stk = []

        for char in s :
            if char in d.values():
                stk.append( char )
            else :
                if not stk or d[char] != stk[-1]:
                    return False
                else:
                    stk.pop()

        return False if stk else True


