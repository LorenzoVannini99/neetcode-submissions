class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs :
            return ""
        
        res = ""
        n = len(strs)
        i = 0
        while i < len(strs[0]) :
            j = 1 
            first_char = strs[0][i]

            while j < n :
                if i >= len(strs[j]) or first_char != strs[j][i]:
                    break
                else :
                    j = j + 1    
            
            if j == n :
                res = res + first_char
                i = i + 1
            else :
                break
        
        return res




        