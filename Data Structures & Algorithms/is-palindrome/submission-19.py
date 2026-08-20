class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s or len(s) == 1:
            return True 
        
        L = 0
        R = len(s) - 1

        while L < R:

            while not s[L].isalnum() and L < R:
                L = L + 1
            while not s[R].isalnum() and L < R:
                R = R - 1
            
            if s[L].lower() != s[R].lower():
                return False
            else :
                L = L + 1
                R = R - 1
                
        return True



