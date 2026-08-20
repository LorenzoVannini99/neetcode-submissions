class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # n = len ( numbers )
        # Idea :
        # use two pointer l and r 
        # l = 0 and r = n - 1
        # From text: " There will always be exactly one valid solution "
        # curr_sum = numbers[l] + numbers[r]  
        # since l < r, numbers[l] < numbers[r]
        # if curr_sum > target --> TOO BIG, r = r - 1
        # else l = l + 1
        
        l = 0
        r = len(numbers) - 1

        while l < r :

            current_sum = numbers[l] + numbers[r]

            if current_sum > target:
                r = r - 1
            elif current_sum < target:
                l = l + 1
            else:
                return [l + 1, r + 1]        






            







        