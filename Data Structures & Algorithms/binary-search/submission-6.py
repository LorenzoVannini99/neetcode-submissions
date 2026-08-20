class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        L = 0
        R = n - 1

        while L < R :
            m = (L + R) // 2
            if nums[m] == target :
                return m
            elif nums[m] > target :
                R = m - 1
            else :
                L = m + 1
        
        if nums[L] == target :
            return L
        else :
            return - 1    