# Brute force
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        S = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if (nums[i], nums[j], nums[k]) not in S:
                            S.add( tuple ( sorted ( [ nums[i], nums[j], nums[k] ] ) ) )
 

        return [list(elements) for elements in S]