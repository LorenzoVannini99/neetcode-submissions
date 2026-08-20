# Problem:
# We have a non empty string s 
# determine if you can delete at most on char to be a palindrome
# OPTIMAL SOL
# do normal two pointers palindrome check
# if a mismatch occurs
# skip left char
# skip right char
# check if they are palindrome
# if not return False
# else go on until L == R
# return True if L == R
# TC : O(n + n + n) = O(n)
# SC : O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if not s or len(s) == 1:
            return True
        
        def isPalindrome(s: str, L, R) -> bool:
            
            if not s or len(s) == 1:
                return True

            while L < R:
                if s[L] != s[R]:
                    return False
                else:
                    L = L + 1
                    R = R - 1

            return True
        
        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return isPalindrome(s, L + 1, R) or isPalindrome(s, L, R - 1)
            else:
                L = L + 1
                R = R - 1


        return True

