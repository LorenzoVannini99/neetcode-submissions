import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        if n2 < n1:
            return False
        
        h1 = {}
        h2 = {}
        
        letters = list(string.ascii_lowercase)

        for char in letters:
            h1[char] = 0
            h2[char] = 0

        # Init s1
        for char in s1 :
            h1[char] += 1
        
        l = 0
        r = n1 - 1
        
        # Init s2
        for char in s2[ l : r + 1 ] :
            h2[char] += 1
        
        if h1 == h2 :
            return True
        
        while r < n2 - 1:

            h2[s2[l]] -= 1
            l += 1

            r += 1
            h2[s2[r]] += 1

            if h1 == h2 :
                return True


        return False






        



 





        