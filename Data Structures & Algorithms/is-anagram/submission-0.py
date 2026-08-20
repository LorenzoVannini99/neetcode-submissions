class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if not s :
            if not t :
                return True
            else :
                return False    

        from collections import Counter

        hash_s = Counter ( s )
        hash_t = Counter ( t )

        if hash_s == hash_t :
            return True
        else :
            return False    


        