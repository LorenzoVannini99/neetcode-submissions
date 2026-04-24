class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if not nums:
            return None
        
        if len(nums) == 1:
            return nums[0]
        
        L = 0
        R = len(nums) - 1

        if nums[L] < nums[R]:
            return nums[L]

        while L < R :
            m = (L + R) // 2

            if nums[m] > nums[R] :
                L = m + 1
            else :
                R = m
             
        return nums[L]
