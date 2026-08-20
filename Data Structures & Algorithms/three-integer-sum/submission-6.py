# Brute force
# sort triplets to mantain order
# only hashable types can be put in set, not list
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        S = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets = ( nums[i], nums[j], nums[k] )
                        if  triplets not in S:
                            S.add( tuple ( sorted ( [ nums[i], nums[j], nums[k] ] ) ) )
 

        return [list(elements) for elements in S]