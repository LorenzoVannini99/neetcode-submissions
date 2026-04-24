# Idea :
# In rotated sorted array, the array is sorted after a certain index j
# j | nums[j] < nums[j - 1]
# L = 0
# R = len(nums) - 1
# to find a target in a sorted array
# L = 0
# R = n - 1
# while L <= R :
#   m = (L + R) // 2
#   if nums[m] == target :
#       return m
#   elif nums[m] > target :
#       R = m - 1
#   else :
#       L = m + 1
# return - 1
# if nums[L] > nums[R], array is not sorted ( or shifted k | k % n == 0)
#
# Let's find the pivot j
# after j just see where the target lies
# and perform BS 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L, R = 0, len(nums) - 1
        
        def binary_search(L, R, target) :

            while L <= R :

                m = (L + R) // 2

                if nums[m] == target :
                    return m
                elif nums[m] > target :
                    R = m - 1
                else :
                    L = m + 1

            return - 1    

        def find_piovot(L, R, nums):


            while L < R :
                m = ( L + R ) // 2

                if nums[m] > nums[R] :
                    L = m + 1
                else :
                    R = m

            return L

        # Now L is the number such that
        # nums[L] < nums[L - 1]

        pivot = find_piovot(L, R, nums)

        res_1 = binary_search(0, pivot - 1, target)
        res_2 = binary_search(pivot, len(nums) - 1, target)

        if res_1 != - 1 :
            return res_1
        elif res_2 != -1 :
            return res_2
        else:
            return - 1      








        