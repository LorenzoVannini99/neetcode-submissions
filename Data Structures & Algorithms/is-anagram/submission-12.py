# Suboptimal Solution
# give two strings
# if they are anagrams they are the same if sorted
# n = len(s), m = len(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # edge cases
        if s and not t or t and not s or len(s) != len(t):
            return False
        elif not s and not t:
            return True

        return sorted(s) == sorted(t)

# k = max(n, m)
# TC : O(klogk)
# SC : O(k)