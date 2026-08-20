class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Idea
        # Sliding Window Approach
        # You have two pointers, L and R
        # When is a window valid?
        # most_seen + k >= window_length

        d = defaultdict(int)

        L , R = 0, 0
        
        most_seen = 0
        res = 0

        while R < len(s):
            
            d[s[R]] += 1
            most_seen = max( most_seen, max(d.values()) )

            while most_seen + k < (R - L + 1):
                d[s[L]] -= 1
                most_seen = max( most_seen, max(d.values()) )
                L = L + 1

            res = max( res, R - L + 1)
            R = R + 1

        return res










            

 
        








        
        
        
        
        