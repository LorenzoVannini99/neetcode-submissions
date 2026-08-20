class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s or len(s) == 1:
            return True
        
        pure_chars = [ char.lower() for char in s if char.isalnum() ]
        s_pure = ''.join(pure_chars)

        return s_pure == s_pure[::-1]




