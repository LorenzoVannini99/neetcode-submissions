class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping closing brackets to opening brackets
        d = {")": "(", "]": "[", "}": "{"}
        stk = []
        
        for char in s:
            if char in d.values():  # Opening bracket
                stk.append(char)
            elif char in d.keys():  # Closing bracket
                if stk and stk[-1] == d[char]:
                    stk.pop()
                else:
                    return False
            else:
                return False  # Invalid character (optional)
        
        return len(stk) == 0
