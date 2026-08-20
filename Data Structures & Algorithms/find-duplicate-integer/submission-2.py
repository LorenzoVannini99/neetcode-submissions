class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # First approach : sorting

        nums.sort()

        s = set()

        for number in nums :
            if number not in s :
                s.add( number )
            else :
                return number   

    
    # TC : O( nlogn )
    # SC : O( n )
   







