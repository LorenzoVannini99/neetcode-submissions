class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        Set = set()
        l = 0
        max_length = 0

        for r in range( len(s) ) :
            while s[r] in Set : 
                Set.remove( s[l] )
                l = l + 1
            Set.add( s[r] )
            max_length = max ( max_length , len(Set))

        return max_length    






        
        