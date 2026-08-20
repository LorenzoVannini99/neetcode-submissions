class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums :
            return None

        hash_map = {}

        for index , value in enumerate ( nums ) :
            res = target - value

            if not res in hash_map :
                hash_map [ value ] = index
            else :
                return [ hash_map [ res ] , index ]

        # TC : O ( n )
        # SC : O ( n )        
 