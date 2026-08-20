# Fast Solution :
# use a set
# if the element is not in the set, put the element in it
# if it is already in the set, return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums or len(nums) == 1:
            return False

        S = set()

        for number in nums:
            if number not in S:
                S.add(number)
            else:
                return True    

        return False

# TC : O(n)
# SC : O(n)