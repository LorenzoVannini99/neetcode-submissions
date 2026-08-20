class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0 or len(nums) == 1 :
            return len(nums)
        
        s = set(nums)
        res = 0

        for n in nums :
            if n - 1 not in s :
                count = 0
                curr = n
                while curr in s :
                    count = count + 1
                    curr = curr + 1 
                    
                res = max ( res , count)


        return res


    