# Python sol with full explanation 
# Simple idea
# L = 0
# R = len(s) - 1
# go left until you find an alphanumeric char R = R - 1
# go right until you find an alphanumeric char L = L + 1
# are they identical? if yes continue
# if not return False
# TC : O(n)
# SC : O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s :
            return True

        L = 0
        R = len(s) - 1

        while L < R:
            while L < R and not ( s[L].isalnum() ):
                L = L + 1
            while L < R and not ( s[R].isalnum() ):
                R = R - 1
            
            if s[L].lower() != s[R].lower():
                return False

            L = L + 1
            R = R - 1
        return True    
