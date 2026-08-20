# Idea :
# The number k represents the replacements you can do
# To create the longest repeating character replacement
# you want to keep track of the char mode.
# The most frequent char that has appeared in a given substring
# The question to ask is : "Is the substring valid?"
# To be valid : len(s) >= R >= L,  and 
# let's pick a certain k_bar
# window length = R - L + 1 = most frequent char count + k_bar
# if the string is valid --> res = window length
# k_bar can take value between 0 and k
# so the string is valid if there are left any k to use
# string is valid if :
# window length - most frequent char count <= k
# Technical details:
# most frequent char count, use a dictionary
# window length = R - L + 1
# if condition is not valid --> L = L + 1
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return None
        elif len(s) == 1:
            return 1
        
        d = {}
        L = 0
        R = 0
        res = 0
        most_freq_char = 0

        while L <= R < len(s):
            char = s[R]

            if char not in d:
                d[char] = 1
            else :
                d[char] += 1

            most_freq_char = max (most_freq_char, d[char])

            while R - L + 1 - most_freq_char > k :
                d[s[L]] -= 1
                L = L + 1
            
            res = max(res, R - L + 1)
            R = R + 1

        return res








