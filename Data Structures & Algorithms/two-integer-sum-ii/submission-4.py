class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if not numbers:
            return 
        
        L = 0
        R = len(numbers) - 1

        while L < R:

            s = numbers[L] + numbers[R]

            if s == target:
                return [L + 1, R + 1]
            elif s > target:
                R = R - 1
            else : 
                L = L + 1
        
        