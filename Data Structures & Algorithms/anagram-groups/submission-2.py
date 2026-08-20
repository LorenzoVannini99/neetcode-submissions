from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)

        if not strs:
            return [[]]

        if n == 1:
            return [[strs[0]]]  
        
        hash_map = {}

        for s in strs :

            sorted_s = ''.join(sorted(s))

            if sorted_s not in hash_map :
                hash_map[sorted_s] = [s]
            
            else :
                hash_map[sorted_s].append(s)

        return hash_map.values()
            

