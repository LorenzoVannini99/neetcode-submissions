class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0 :
            return [[""]]

        elif len(strs) == 1:
            return [strs]
        
        hash_set = {}
        
        for s in strs :

            if tuple(sorted(s)) not in hash_set :
                hash_set[tuple(sorted(s))] = [s]
            else :
                hash_set[tuple(sorted(s))].append(s)
       
        return hash_set.values() 