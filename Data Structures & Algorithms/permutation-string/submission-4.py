import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        if n2 < n1:
            return False

        h1 = {char: 0 for char in string.ascii_lowercase}
        h2 = {char: 0 for char in string.ascii_lowercase}

        for char in s1:
            h1[char] += 1
        for char in s2[:n1]:
            h2[char] += 1

        if h1 == h2:
            return True

        l = 0
        r = n1

        while r < n2:
            h2[s2[l]] -= 1         # Remove char leaving the window
            h2[s2[r]] += 1         # Add new char entering the window
            
            if h1 == h2:
                return True
                
            l += 1
            r += 1



        return False

        



 





        