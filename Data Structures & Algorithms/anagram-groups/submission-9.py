# Sub Optimal
# n = len(strs)
# m = max( [len(s) for s in strs] )
# given two strings s and t
# if sorted are the same, they are anagrams
# create a dictionary, d = {"sorted(s)":[s, t]} for each s and t that are anagrams
# checking time in an hashmap is O(1)
# TC : O( mlogm *n)
# SC : O( n * m)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs :
            return 
        
        hashmap = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if  sorted_s in hashmap:
                hashmap[sorted_s].append(s) 
            else :
                hashmap[sorted_s] = [s]
        
        return list(hashmap.values())
        


        
        
        