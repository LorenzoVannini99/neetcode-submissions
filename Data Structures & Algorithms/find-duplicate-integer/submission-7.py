class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Idea :

        # By definition we know We have a cycle.
        # if we knew how many times more the duplicate numbers appear other techniques would be used
        # if we knew that the duplicate numbers appears k times more

        # Maybe a strategy using the sum of all numbers can be useful S = n(n+1)/2, 
        # and maybe a divide and conquer techniques can be used

        # We only know that it will appear 2 or more times
        # the useful idea is to think it like a linked list

        # index = i, next = nums[i]
        # index = 1, next = nums[1]
        # index = 2, next = nums[2]...
        # Input: nums = [1,2,3,2,2]
        
        # index = 0, next = nums[0] = 1
        # index = 1, next = nums[1] = 2
        # index = 2, next = nums[2] = 3 
        # index = 3, next = nums[3] = 2
        # CYCLE

        # They will meet inside the circle
        # No guarantess they will meet at the beginning of the cycle
        # i.e : No guarantess they will meet at the duplicate number

        # Use Floyd’s cycle-finding algorithm
        # Without go much into detail
        # Floyd’s algorithm finds the meeting point 
        # of slow and fast pointers in a cycle, then finds the cycle entry.
        # since the meeting point between slow and fast
        # and the distance between the entrance and the starting cycle point is the same
        # so if mu = distance between head and cycle
        # Finder is the ptr at the beginning, Finder + mu == slow + mu

        slow = nums[0]
        fast = nums[0]

        while True : # no need to check other things, cycle will be detected
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]

            if fast == slow :
                break
            
        # At this point, slow == fast
        Finder = nums[0]

        while Finder != slow :
            Finder = nums[Finder]
            slow = nums[slow]
        
        return Finder

















