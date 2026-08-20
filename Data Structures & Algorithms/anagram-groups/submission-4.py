from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Idea :
        # n = len(strs)
        # m = average word length
        # k = unique sorted words
        #
        # suboptimal sol
        # create a hashmap with
        # h[sorted(s)].append(s)
        # return [h[words] for words in h.keys()]
        # TC : O(mlogm * n)
        # SC: O (k)
        #
        # Optimal sol 
        # For each word create a unique map, an encoding with words count
        # create a dict, where dict[map] = [words with same encoding]
          
        from collections import defaultdict

        d = defaultdict(list)
        unique = [0] * 26

        for word in strs:
            unique = [0] * 26
            for char in word:
                unique[ord(char) - ord('a')] += 1
            
            unique_tuple = tuple(unique)
            d[unique_tuple].append(word)
        
        return [d[keys] for keys in d.keys() ]



        
        

    







            

