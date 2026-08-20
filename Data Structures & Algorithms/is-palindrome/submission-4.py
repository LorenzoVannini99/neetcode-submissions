class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s or len(s) == 1:
            return True
        
        s_pure = ""

        for char in s:
            if char.isalnum() :
                s_pure = s_pure + char.lower()

        return s_pure == s_pure[::-1]




