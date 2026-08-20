class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s :
            return 0

        if len(s) == 1 :
            return 1    
        
        # Idea :
        # 2 pointers, L and R starting from the position, s[0]
        # we keep track of the longest substring wrc ( window_size and res )
        # we then set window_size = R - L + 1
        # We can use a set to have a unique collections of numbers
        # L is "fixed" and we let R slice to the right
        # if s[R] is not in our set, we update the set and res ( window_size =+ + 1)
        # and res = max ( res, window_size)
        # we keep doing this until we find a repeating char (in our set)
        # we reset window_size and we update L and R position

        res = 1
        window_size = 1

        Set = set()
        
        L = 0
        R = 0
    
        while L <= R < len(s): 

            while L <= R < len(s) and s[R] not in Set :
                Set.add(s[R])
                window_size = R - L + 1
                res = max(res, window_size)
                R = R + 1
                
            while L <= R < len(s) and s[R] in Set :
                Set.remove(s[L])
                L = L + 1
        
        return res









  














        
        