
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Idea 1 :
        # create a Counter
        # store and sort all occurencies
        # take the kth 
    
        if not nums :
            return []

        from collections import Counter
        
        dict_counter = Counter ( nums )
        
        counter_items = [ [numb, occ] for numb,occ in dict_counter.items() ]
        sorted_counter_items = sorted ( counter_items, key = lambda x: x[1], reverse = True )
        
        return [ numb for numb,_ in sorted_counter_items[:k] ]




        
        







