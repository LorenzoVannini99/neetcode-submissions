class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # n = len(s)
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
        # if you at each char and stk is not empty you can remove the "(" or ")"
        # s.remove(index)

        if not s:
            return s

        stk = []
        remove_index_list = []

        for i in range ( len(s) ):
            if s[i] == "(":
                stk.append(i)

            if s[i] == ")" :
                if not stk :
                    remove_index_list.append(i)  
                else :
                    stk.pop()

        list_s = list(s)

        for index in sorted(stk + remove_index_list, reverse = True):
            list_s.pop(index)

        return "".join(list_s)