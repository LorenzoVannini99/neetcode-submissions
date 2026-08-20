from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n2 < n1:
            return False

        d1 = Counter(s1)

        for i in range(n2 - n1 + 1):  # includes the last valid window
            if Counter(s2[i:i + n1]) == d1:
                return True

        return False

        



 





        