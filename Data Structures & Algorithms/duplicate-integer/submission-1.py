class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        n = len ( nums )

        if n == 0 :
            return False

        if n == len ( set (nums) ) :
            return False
        else :
            return True    