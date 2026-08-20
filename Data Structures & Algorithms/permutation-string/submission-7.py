import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        m = len(s1)
        n = len(s2)

        if n < m :
            return False
        
        # Aiming for TC : O(n) , SC : O(1)
        # If SC : O(1) we cannot use a Counter ( from collection import Counter )
        
        # Alphabet count for s1
        alph1_count = [0] * 26

        for char in s1 :
            alph1_count[ord(char) - ord('a')] += 1 
        
        # Sliding Window approach

        l = 0
        r = m - 1

        # Alphabet count for first substring
        alph2_count = [0] * 26

        for char in s2[l:r + 1] :
            alph2_count[ord(char) - ord('a')] += 1         
        
        if alph1_count == alph2_count :
            return True
        else :

            while r < n - 1 :

                # remove left char
                alph2_count[ord(s2[l]) - ord('a')] -= 1

                l = l + 1
                r = r + 1

                # add new right char
                alph2_count[ord(s2[r]) - ord('a')] += 1

                if alph2_count == alph1_count :
                    return True



            return False





        



 





        