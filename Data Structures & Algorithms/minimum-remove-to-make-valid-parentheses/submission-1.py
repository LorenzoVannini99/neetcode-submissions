class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # n = len(s)
        # k = number of elements to remove
        #
        # Idea :
        # given s, if it is empty return s
        # if it is not empty
        # create an empty stk = []
        # look each char in s
        # if it is a simple lower case char --> VALID
        # if at some index i you find char = "("
        # stk = [ ( "(", i ) ]
        # if at index j > i you find ")"
        # stk.pop()
        # if you find a char and stk is not empty you can remove the "(" or ")"
        # s.remove(index)
        # TC : O(n)
        # SC : O(n)


        if not s :
            return s
        
        stk = []

        # Track indices of parentheses to remove
        for i, char in enumerate(s):
            if char == "(":
                stk.append(i)  # store index
            elif char == ")":
                if stk and s[stk[-1]] == "(":
                    stk.pop()  # matched pair
                else:
                    stk.append(i)  # unmatched closing parenthesis

        list_s = list(s)

        while stk:
            del list_s [stk[-1]]
            stk.pop()

        return "".join(list_s)   
            











        