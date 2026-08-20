class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums :
            return None
 
        h = {}

        for index,number in enumerate ( nums ) :

            residual = target - number

            if residual in h :
                return [h[residual],index]
            else:
                h[number] = index
