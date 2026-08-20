class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        if not s :
            if not t :
                return True
            else :
                return False    

        hash_s = {}
        hash_t = {}

        for char in s : 
            if char in hash_s :
                hash_s[char] = hash_s[char] + 1
            else :
                hash_s[char] = 1

        for char in t : 
            if char in hash_t :
                hash_t[char] = hash_t[char] + 1
            else :
                hash_t[char] = 1

        if hash_s == hash_t :
            return True
        
        else :
            return False
        