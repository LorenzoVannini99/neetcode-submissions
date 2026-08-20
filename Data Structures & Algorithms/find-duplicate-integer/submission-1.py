class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Step 1: Find the intersection point (cycle detection)
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]        # move 1 step
            fast = nums[nums[fast]]  # move 2 steps
            if slow == fast:
                break
        
        finder = nums[0]

        while finder != slow :
            finder = nums[finder]
            slow = nums[slow]

        return finder
   







