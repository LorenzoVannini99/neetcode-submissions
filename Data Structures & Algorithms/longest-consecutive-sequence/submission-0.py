class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        max_length = 0

        for number in nums :
            if number in s :
                current = number
                length = 1

                while current + 1 in s :
                    length = length + 1 
                    current = current + 1
            
            max_length = max ( max_length , length)

        return max_length 
                
            
                