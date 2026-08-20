class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        l = 0
        r = n - 1

        while l < r : 
            while not s[l].isalnum() and l < r  :
                l = l + 1
            while not s[r].isalnum() and l < r:
                r = r - 1
            
            if s[l].lower() != s[r].lower() :
                return False
            else :
                l = l + 1
                r = r - 1

        return True










