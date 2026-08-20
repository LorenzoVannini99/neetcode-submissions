class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Idea:
        # Use 2 pointers L and R
        # L starts at 0
        # R starts at n - 1
        # from right: go to the left until you see an a letter or number
        # from left : go right  until you see a letter or number
        # if they are not equal return False
        # else --> go on
        # TC: O(n)
        
        n = len(s)

        L = 0
        R = n - 1
        
        s = s.lower()

        while L < R :
            while L < R and not s[L].isalnum():
                L = L + 1
            while L < R and not s[R].isalnum():
                R = R - 1

            if s[L] != s[R] :
                return False
            else :
                L = L + 1
                R = R - 1

        return True        











