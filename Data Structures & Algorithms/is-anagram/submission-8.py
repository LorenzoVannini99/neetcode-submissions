# Hashmap optimal solution
# n = len(s)
# m = len(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if s and not t or t and not s or(len(s) != len(t)):
            return False
        elif not s and not t:
            return True
        
        d_s = {}
        d_t = {}
        
        # init
        for i in range(len(s)):
            d_s[s[i]] = 0
            d_t[t[i]] = 0
        
        for i in range(len(s)):
            d_s[s[i]] += 1
            d_t[t[i]] += 1
        
        if d_s == d_t : 
            return True
        else :
            return False    
        
        # TC : O( n + m )
        # SC : O( 1 )
