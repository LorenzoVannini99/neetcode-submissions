class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return min(nums)
        
        if nums[0] < nums[n - 1]:
            return nums[0]

        l = 0
        r = n - 1

        res = nums[0]

        while l <= r :
            # if portion is sorted
            if nums[l] < nums[r] :
                res = min(res,nums[l])
                break

            mid = ( l + r ) //2
            res = min(res,nums[mid])

            # from l to mid the array is sorted
            if nums[mid] >= nums[l]:
                l = mid + 1
            else :
                r = mid - 1

        return res

