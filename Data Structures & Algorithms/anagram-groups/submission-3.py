from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs:
            return [[]]

        if len(strs) == 1:
            return [[strs[0]]]

        hash_map = defaultdict(list)

        for s in strs:
            count_alphabet = [0] * 26
            for char in s:
                count_alphabet[ord(char) - ord('a')] += 1
            hash_map[tuple(count_alphabet)].append(s)

        return list(hash_map.values())


            

