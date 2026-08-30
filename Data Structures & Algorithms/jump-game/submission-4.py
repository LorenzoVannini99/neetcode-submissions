"""
# Idea :
Let's call i the index of the number, i = 0,..., len(nums) - 1.

At step i = 0, you can jump at most i = 0 + nums[i = 0]

If nums[0] = 0 return False.

At each step you have a reachability window, you can start from i and you should try to go as far as possible. 

Each number can give you a reachability based on their value and their position of :
    R = max(R, i + nums[i])

R is an index among the possible indexes and is the furthest integer I can reach, if at some point, by traversing the array, i > R, there is an index I am visting that is beyond my reachability. Just return False

Every number is traversed once and no other operation is done --> linear time complexity .
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:

     
        R = 0

        for i in range(len(nums)):
            
            if R < i :
                return False

            R = max(R, i + nums[i] )

        return True




        