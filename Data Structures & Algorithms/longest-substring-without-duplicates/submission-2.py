class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s :
            return 0

        if len (s) == 1 :
            return 1    
        
        valid_set = set ()
        l = 0
        r = 0
        max_length = 0

        while l <= r < len ( s ) :

            while s[r] in valid_set :
                valid_set.remove(s[l])
                l = l + 1
            
            valid_set.add(s[r])
            max_length = max ( max_length , r - l + 1)
            r = r + 1


        return max_length
           












        
        