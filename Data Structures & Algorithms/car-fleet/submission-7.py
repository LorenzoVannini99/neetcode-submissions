# Idea :
# put everything in a nice list sorted by position
# l = [ (pi, vi) ] for all i
# then calculate time to reach the target
# ti = floor ( (target - pi) / vi )
# put the time ti in a stack
# if a j exist such that tj > ti, pop ti and put tj
# tj is the next greater time, thus the next fleet
import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        l = [ (pi, vi) for pi, vi in zip(position, speed) ]
        l = sorted(l, key = lambda x : x[0], reverse = True)

        stk = []
        res = 0

        for p, v in l:
            time_to_go = ( (target - p) / v )
            if not stk or time_to_go > stk[-1]:
                stk.append(time_to_go)
                

        return len(stk)
        


        