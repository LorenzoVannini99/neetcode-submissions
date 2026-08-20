class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # same idea:
        # two pointers
        # move l and r such that they are valid
        # what does valid mean?, no repeating char
        # if there is no repeating char, move R to the right
        # if it is nit valid move L to the right until it's valid
        # use a set for uniquness and for fast lookup O(1)
        
        # edge cases
        if not s :
            return 0
        if len(s) == 1:
            return 1
        
        S = set()

        L = 0
        R = 0

        max_length = 0

        while L <= R < len(s):

            while R < len(s) and s[R] not in S:
                S.add(s[R])
                max_length = max(max_length, R - L + 1)
                R = R + 1

            while R < len(s) and s[R] in S:
                S.remove(s[L])
                L = L + 1 
        
        return max_length











  














        
        