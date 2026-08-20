class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        from collections import Counter

        d1 = Counter (s1)
        n1 = len (s1)
        n2 = len(s2)

        for i in range (n2 - n1 + 1) :
            window = s2[i:i + n1]
            d2 = Counter(window)

            if d1 == d2 :
                return True

        return False        





        