class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if not nums:
            return None
        
        if len(nums) == 1:
            return nums[0]
        
        L = 0
        R = len(nums) - 1

        while L < R :
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else :
                R = mid

        return nums[L]