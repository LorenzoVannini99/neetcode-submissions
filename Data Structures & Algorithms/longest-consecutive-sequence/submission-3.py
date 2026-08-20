class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len ( nums )
        
        if not nums :
            return 0

        if n == 1 :
            return 1    

        s = set ( nums )
        res = 0

        for n in nums :
            
            if n - 1 not in s:
                counter = 0
                curr = n 

                while curr in s :
                    counter = counter + 1
                    curr = curr + 1
                
                res = max ( res , counter)

                
        return res    
                