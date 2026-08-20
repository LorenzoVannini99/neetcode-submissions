class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Idea :
        # L = [(pi,vi)] for all i = 1,..,n
        # Sort in descending order an take in cosideration time to reach target
        # call this time t_i
        # t_i = (target - p_i) / v_i
        # stk = [t_i], fleet = 1
        # if exist a j such that t_j > t_i, fleet = fleet + 1
        # repeat for all position
        # TC : O(n + nlogn)
        # SC : O(n)
        
        pos_speed = [(p,v) for p,v in zip(position, speed)]
        pos_speed_sorted = sorted(pos_speed, key = lambda x: x[0], reverse = True)
        
        fleet = 0
        last_time = - 1

        for (p,v) in pos_speed_sorted:

            t = ( target - p ) / v

            if t > last_time :
                last_time = t
                fleet = fleet + 1

        return fleet   




        

         
       
    