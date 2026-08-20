import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Idea :
        # n = len (s1), m = len(s2)
        #
        # Brute force solution :
        # sort everysubstring and compare 
        # --> TC : O ( (m - n) * nlog(n) ) if m >> n --> O(m*n*log(n))
        #
        # Suboptimal solution :
        # Use a hashmap, use a Counter
        # create a Counter for s1 and every substring of s2
        # TC : O (n + n*(m - n)), if m >> n --> O ( m*n )
        # SC : O ((m-n) * n), if m >> n --> O ( 26 )
        # 
        # Optimal solution :
        # Implement a hashfunction by creating a 26 long tuple
        # is an encoding of a substring
        # It's a clever way to create and compare a unique identifier for words
        # abc = (1,1,1,0,..,0), bbb =(0,3,0,...,0) and so on 
        # we let L and R slides and modify the tuple
        # every slide is at most O(2) * (m - n)
        # if tuple s1 == tuple s2 --> return True
        # TC : O( m )
        # SC : O( 26 )
        #
        #
        
        n = len(s1)
        m = len(s2)

        if n > m :
            return False

        s1_enc = [0] * 26
        s2_enc = [0] * 26

        for i in range(n):
            s1_enc[ ord(s1[i]) - ord('a') ] += 1
            s2_enc[ ord(s2[i]) - ord('a') ] += 1
        
        if s1_enc == s2_enc :
            return True
        
        for i in range (n, m):
            s2_enc[ ord(s2[i]) - ord('a') ] += 1
            s2_enc[ ord(s2[i - n]) - ord('a') ] -= 1

            if s2_enc == s1_enc :
                return True

        return False






        


        



 





        