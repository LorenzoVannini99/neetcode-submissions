class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}  # val : index
        
        # using enumerate to create a pair ( index , value )

        for index , value in enumerate ( nums ) :

            residual = target - value

            if residual in hash_map :

                return [ hash_map [residual] , index ]
            
            else :

                hash_map [ value ] = index
