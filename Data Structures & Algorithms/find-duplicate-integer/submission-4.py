class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #Hash set
        s = set()

        for number in nums :
            if number not in s:
                s.add(number)
            else :
                return number    

        # TC : O( n )
        # SC : O( n )








