# hashmap Solution
# give two strings
# if they are anagrams, their counter is identical

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # edge cases
        if s and not t or t and not s:
            return False
        elif not s and not t:
            return True

        from collections import Counter

        if Counter(s) == Counter(t):
            return True
        else :
            return False

# k = max(n, m)
# TC : O(k)
# SC : O(k)