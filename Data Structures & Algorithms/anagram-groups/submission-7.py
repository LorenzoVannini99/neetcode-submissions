# Sorting Solution
# n = len(strs)
# m = max( [len(s) for s in strs] )
# given two strings s and t
# if sorted are the same, they are anagrams
# create a dictionary, d = {"sorted(s)":[s, t]} for each s and t that are anagrams
# checking time in an hashmap is O(1)
# TC : O( mlogm *n)
# SC : O( n )

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}

        for s in strs:
            sorted_s = sorted(s)
            sorted_string = ''.join(sorted_s)
            if sorted_string not in d:
                d[sorted_string] = [s]
            else:
                d[sorted_string].append(s)
        
        return list(d.values())


        
        
        