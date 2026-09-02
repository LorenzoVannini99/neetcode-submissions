"""
Optimal solution :

No need to go to the sorted solution.
if two sorted strings are equal they have the same counter.

A counter is a dictionary where you have d = { "char" : char_counter }

Very hard to hash this or use it.

You can do something similar by exploiting ord(char).
ord(char) is a unique number, ord(a) - ord(a) is 0, ord(z) - ord(a) = 25.

Remember to use a tuple to use an immutable key.


TC : O ( n * m )
SC : O ( n )

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for s in strs:

            count = [0] * 26

            # TC : O(26)
            for char in s:
                count[ ord(char) - ord("a") ] += 1
            
            key = tuple(count)

            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]

        
        return list ( hashmap.values() )



        