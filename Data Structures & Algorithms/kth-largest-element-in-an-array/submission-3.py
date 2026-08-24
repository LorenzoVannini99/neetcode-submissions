# First non optimal sol

# Sort the array
# TC : O(nlogn)
# SC : O(n)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort()

        return nums[-k]
        