class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (not s1 and s2) or (not s2 and s1):
            return False
        elif not s1 and not s2:
            return True
       
        from collections import Counter
       
        m = len(s1)
        n = len(s2)

        d1 = Counter (s1)
       
        L = 0
        R = m - 1
       
        for i in range (n):
            substring = s2[i:i+m]
            d2 = Counter (substring)
            if d1 == d2 :
                return True

        return False
      
