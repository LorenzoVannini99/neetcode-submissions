# Idea :
# if array is sorted, easier to skip duplicate
# if one element is fixed
# the problems is two sum
# where target is the - number fixed
# TC : O(n^2)
# SC : O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            # skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            L = i + 1
            R = n - 1

            while L < R:
                current_sum = nums[L] + nums[R]

                if current_sum == target:
                    result.append([nums[i], nums[L], nums[R]])

                    L += 1
                    R -= 1

                    # skip duplicates on the left
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

                    # skip duplicates on the right
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

                elif current_sum < target:
                    L += 1
                else:
                    R -= 1

        return result


