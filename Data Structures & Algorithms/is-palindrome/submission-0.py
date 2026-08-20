class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1 = ""

        for c in s :
            if c.isalnum() :
                s1 = s1 + c.lower()

        return s1 == s1[::-1]        