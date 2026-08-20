class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len ( nums )

        if n == 0 :
            return -1
        if n == 1:
            if nums[0] == target :
                return 0
            else:
                return -1        
        
        l = 0
        r = n - 1

        while l <= r :
            mid = ( l + r ) // 2

            if target == nums[mid] :
                return mid
            elif target < nums[mid] :
                r = mid - 1
            else :
                l = mid + 1

        return -1       


        