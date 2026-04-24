# Optimal Solution
# Use fixed 26 char letters array
# ord in Python converts a character into its corresponding integer code point.
# ord(c) = Unicode code point of character c
# example : ord('a') = 97
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # edge cases
        if s and not t or t and not s or len(s) != len(t):
            return False
        elif not s and not t:
            return True

        arr = [0] * 26
        
        for i in range(len(s)):
            arr[ ord(s[i]) - ord("a") ] += 1
            arr[ ord(t[i]) - ord("a") ] -= 1

        for val in arr:
            if val != 0:
                return False
        
        return True

# k = max(n, m)
# TC : O(k)
# SC : O(26)