class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()

        for k in range(n):
            target = -nums[k]
            hash_map = {}
            for i in range(k + 1, n):  # Only look at elements after k
                value = nums[i]
                residual = target - value
                if residual in hash_map:
                    triplet = tuple(sorted([nums[k], value, residual]))
                    res.add(triplet)
                hash_map[value] = i  # Save value for lookup

        return [list(triplet) for triplet in res]







        


        