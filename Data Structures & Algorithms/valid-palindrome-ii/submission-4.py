# Problem:
# We have a non empty string s 
# determine if you can delete at most on char to be a palindrome
# SOL
# do normal two pointers palindrome check
# if a mismatch occurs
# skip left char
# skip right char
# check if they are palindrome
# if not return False
# else go on until L == R
# return True if L == R
# TC : O(n + n + n) = O(n)
# SC : O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True
        
        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] == s[R]:
                L = L + 1
                R = R - 1
            else:
                l_string = s[L + 1: R + 1]
                r_string = s[L: R]

                if l_string == l_string[::-1] or r_string == r_string[::-1]:
                    return True
                else:
                    return False
                
        return True

