from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Idea :
        # Suboptimal idea
        # By sorting strings we can check easier anagrams
        # k = unique strings in strs
        # n = len(strs)
        # m = average words length
        
        # TC : O(mlogm * n)
        # SC : O(n + k)


        d = defaultdict(list)

        for s in strs:

            sorted_list = sorted(s)
            sorted_strings = "".join(sorted_list)

            if sorted_strings in d:
                d[sorted_strings].append(s)

            else :
                d[sorted_strings] = [s]

        return list(d.values())








        
        

    







            

