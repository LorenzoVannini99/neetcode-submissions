"""
# Optimal Solution :
Let's call i the index of the number, i = 0,..., len(nums) - 1.

At step i = 0, you can jump at most i = 0 + nums[i = 0]

If nums[0] = 0 return False.

At each step you have a reachability window, you can start from i and you should try to go as far as possible. 

Each number can give you a reachability based on their value and their position of :
    R = max(R, i + nums[i])

R is an index among the possible indexes and is the furthest integer I can reach, if at some point, by traversing the array, i > R, there is an index I am visting that is beyond my reachability. Just return False

Every number is traversed once and no other operation is done --> linear time complexity .

## Why taking the max can lead to a wrong solution?
If $$ R_i = 0≤j≤i max​(R, nums[j] ) $$
I choose the largest element that can lead to the highest jump but is not necessarily the furthest possible jump.

if nums[4,5,0,0,4,...], the index i = 4 can create the furthest jump, not the maximum local jump.

## Why does greedy here work?
If two reachability R1 and R2 are compared, the R_max = max(R2, R1) dominates, It is always better to go as further as possible, since if an optimal index exist, the R_min = min(R1, R2) is a subset of R_max will contain that solution. 

$$ {0,…,Rmin}⊆{0,…,Rmax} $$

Therefore, every position reachable with $R_{min}$ is also reachable with $R_{max}$.

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        R = 0

        for i in range(len(nums)):
            
            if R < i :
                return False

            R = max(R, i + nums[i] )

        return True




        