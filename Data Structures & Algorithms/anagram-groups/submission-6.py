from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Idea :
        # Optimal idea
        # We need a unique hashable encoding such that
        # each word is uniquely identified by their char apperances
        # unique ( aabcz ) = (2, 1, 1, 0,...,0,..,1)  outputs a tuple of 26 chars
        # by doing this i do not have to sort the strings avoid n*mlogm TC
        
        # m = average word length
        # n = len(strs)
        # k = uniue chars in strs

        # TC : O(n * m)
        # SC : O(26 + k) = O(k)

        def unique(s):
            res = [0] * 26

            for char in s:
                res[ ord(char) - ord('a')] += 1

            return tuple(res)
        
        d = defaultdict(list)

        for s in strs:

            unique_tuple = unique(s)

            if unique_tuple in d:
                d[unique_tuple].append(s)
            else :
                d[unique_tuple] = [s]

        return list(d.values())        








        
        

    







            

