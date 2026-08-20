class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Idea :
        # We can use a hashmap to keep track of the most visited char in the window
        # using a d = defaultdict(int), d[char] = count
        # L,R start from 0, first char is s[0]
        # we then update R, let it slice to the right if is valid
        # a window is valid if k >= ( number of non most used char )
        # if k is greater than the number of things i can replace
        # the window is valid 
        # i can "think" like i have k char to replace
        # so i can act as if the different chars
        # does not exist and can be replaced.
        # Validation Condition : k >= ( (R - L + 1) - most visited char )
        
        if not s :
            return 0
        
        if k == len(s) :
            return len(s)
        
        d = defaultdict(int)

        res = 1
        max_char_count = 0

        L = 0
        R = 0

        for R in range(len(s)) :
            d[s[R]] += 1
            max_char_count = max(max_char_count, d[s[R]])

            # shrink window if invalid
            while (R - L + 1) - max_char_count > k:
                d[s[L]] -= 1
                L += 1

            # window is valid here
            res = max(res, R - L + 1)
        

        return res


        








        
        
        
        
        