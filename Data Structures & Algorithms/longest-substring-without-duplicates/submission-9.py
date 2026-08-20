# Idea :
# n is the length of the string 
# m is the number of unique characters in the string.
# There might be different solutions
# You can create a counter for each substring and 
# check whether the counter.values() are between 0 and 1
# but TC : O( m * n )
# using a sliding window approach is better
# use a set S to identify unique numbers
# L = 0
# R = 0
# res = 0
# while R < len(s):
#   if char not in S:
#       substring is valid
#       move R to the right
#       res = res + 1
#   else :
#   move L to the right until the substring is valid
# return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
        
        hashset = set()
        L = 0
        R = 0
        res = 0

        while R < len(s):

            while R < len(s) and s[R] not in hashset:
                res = max(res, R - L + 1)
                hashset.add(s[R])
                R = R + 1
                
            while L <= R < len(s) and s[R] in hashset:
                hashset.remove(s[L])
                L = L + 1
        
        return res
        











        