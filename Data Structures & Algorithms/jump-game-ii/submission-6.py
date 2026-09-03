"""
# OPTIMAL SOL :

We can do something similar to BFS levels:

$$ \text{all positions reachable in 1 jump}} $$

then

$$ \text{all positions reachable in 2 jumps}} $$

then

$$ {\text{all positions reachable in 3 jumps}} $$

You only move to the next level after completely processing the current one.

The key line is:

    if i == current_end:

At that moment, you've processed the entire range reachable with the current number of jumps, so you commit to the next jump.

## Intuition :
At each level you create a range of possible numbers that I can reach, I only increase jumps if I move to the next range, the next frontier.


"""

class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        current_farthest = 0
        farthest = 0

        for i in range( len(nums) - 1):
            farthest = max( farthest, i + nums[i] )

            if i == current_farthest:
                jumps += 1
                current_farthest = farthest


        return jumps




        