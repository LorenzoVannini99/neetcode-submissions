# Suboptimal Solution :
# The solution is guaranteed to exists
# There must be 2 indices i,j st nums[i] + nums[j] == target
# sort the array
# Use two pointers technique
# remember to keep track of original indices
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        arr = [(val, idx) for idx, val in enumerate(nums)]
        arr.sort()  
        
        L, R = 0, len(arr) - 1
        
        while L < R:
            s = arr[L][0] + arr[R][0]
            
            if s == target:
                return sorted ( [arr[L][1], arr[R][1]] )
            elif s < target:
                L += 1
            else:
                R -= 1

# TC : O(nlog(n))
# SC : O(n)