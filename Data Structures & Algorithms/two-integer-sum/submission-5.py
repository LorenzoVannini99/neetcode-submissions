class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Idea :
        # If two numbers sum up to target nums[i] + nums[j] = target
        # the brute force solution is just to search if the residual
        # residual = target -  nums[j] is in nums[i : ] for all i
        # TC : O ( (n-1) + n-2 + ...) = O(n^2), SC : O(1)
        # think about it, if  exist i,j st nums[i] + nums[j] = target
        # if you move all i,j -_> O(n^2) you are sure to find it
        # but you only need ONE PASS 
        # just pass through the array once and use a hashmap 
        # i = 0 
        # if res = target - nums[i] in hashmap, WE ARE DONE
        # if not hashmap[number] = i 
        # hashmap[number] = i --> " If you find at a particual index that res in hashmap,"
        # "the index such that nums[i] + nums[index] = target is hashmap[number]"
        # hashmap is just a way to store and retrieve in O(1) the residuals
        # and just return [i, index]
        # This works because sum is commutative, meaning that a + b = b + a
        # TC : O(n)
        # SC : O(n)

        if not nums:
            return

        hashmap = { }

        for index,number in enumerate ( nums ) :

            res = target - number

            if res not in hashmap :
                hashmap[number] = index

            else :
                return [hashmap[res], index ]






