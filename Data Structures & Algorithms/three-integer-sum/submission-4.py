class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort() # TC: O(n) and SC: O(1)
        results = []

        for k in range ( n ):

            if nums[k] > 0 :
                break
            
            if 0 < k and nums[k] == nums[k-1] :
                continue 
            
            target = - nums[k]
            l = k + 1
            r = n - 1

            while l < r :
                curr_sum = nums[l] + nums[r]

                if curr_sum == target :
                    triplets = [nums[l],nums[r],nums[k]]
                    results.append(triplets)
                    
                    l += 1
                    r -= 1

                    while l < r and nums[l-1] == nums[l] :
                        l += 1
                    while 0 < l < r < n and nums[r] == nums[r+1] :
                        r -= 1

                elif curr_sum < target :
                    l += 1
                else :
                    r -= 1    

        return results








        


        