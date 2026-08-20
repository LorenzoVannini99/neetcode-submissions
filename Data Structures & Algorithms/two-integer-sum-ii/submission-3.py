# Idea:
# n = len(nums)
# Given a non empty and non decreasing list of integers
# Find two indices such that numbers[index1] + numbers[index2] == target
# As stated in the problem : "There will always be exactly one valid solution."
# L = 0
# R = len(nums) - 1
# sum = numbers[L] + numbers[R]
# numbers[L] <= numbers[R]
# if sum == target --> return L + 1, R + 1
# if sum < target
# increase the sum --> increase L
# if sum > target
# decrease the sum --> decrease R
# TC : O(n)
# SC : O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        L = 0
        R = n - 1

        if numbers[L] == numbers[R]:
            if numbers[L] + numbers[R] == target:
                return [L + 1, R + 1]

        while L < R:
            summation = numbers[L] + numbers[R]

            if summation == target:
                return [L + 1, R + 1]
            elif summation < target:
                L = L + 1
            else :
                R = R - 1 

            













    
