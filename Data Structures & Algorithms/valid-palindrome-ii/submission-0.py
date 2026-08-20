# Problem:
# We have a non empty string s 
# determine if you can delete at most on char to be a palindrome
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True
        
        def isPalindrome(l: List) -> bool:
            if not l or len(l) == 1:
                return True

            L = 0
            R = len(l) - 1

            while L < R:
                if l[L] != l[R]:
                    return False
                else:
                    L = L + 1
                    R = R - 1

            return True

        list_s = list(s)

        for i in range(len(s)):
            list_to_check = list_s[:i] + list_s[i + 1:]
            if isPalindrome(list_to_check):
                return True
        
        return False



