# Sorting solution
# n = len(s)
# m = len(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if s and not t or t and not s or(len(s) != len(t)):
            return False
        elif not s and not t:
            return True
        
        if sorted(s) == sorted(t):
            return True
        else :
            return False
        
        # TC : O(nlogn + mlogm)
        # SC : O(1)
