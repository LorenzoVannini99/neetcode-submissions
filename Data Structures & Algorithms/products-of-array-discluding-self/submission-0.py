class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Suboptimal solution optimized
        n = len(nums)

        left = [0] * n
        left[0] = 1

        right = [0] * n
        right[n - 1] = 1

        output = [0] * n

        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
            right[n - 1 - i] = right[n - i]*nums[n - i]
        
        
        return [l*r for l,r in zip(left, right)]












