class Solution:
    def isValid(self, s: str) -> bool:

        # Idea :
        # Create a stack for open brackets
        # once a closed bracket is found, 
        # if does not match last stack element --> False

        dictionary = { "}" : "{", ")" : "(", "]" : "[" }
        stack = []

        for char in s :
            if char in dictionary.values() :
                stack.append( char )
            else :
                if stack:
                    last_element = stack.pop()
                    if dictionary[char] != last_element :
                        return False
                else:
                    return False
                    
        if stack:
            return False
        else :
            return True    
                    



          