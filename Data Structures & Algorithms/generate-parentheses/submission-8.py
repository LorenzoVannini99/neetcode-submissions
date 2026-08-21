#                 Visual idea :
#                  curr = "("
#                /           \
#        "(("                  "()"

# The idea is pretty simple
# go left  or right if you can
# when can you left or right?
# the valid condition is that the number of close >= open
# Let's say you start with a close
# close < open --> wrong
# Let's say you have one open and 2 close --> wrong
# That's it
# make sure to understand when s a string or a condition is valid
# simply then pass to dfs
# very similar to other tree problems

# You do not even need to do list.pop()
# In python string are immutable
# an immytabke object cannot be changed
# doing curr = curr + "(" is creating a new object
# the name curr in the stack is point to a different object in the heap
# Quite usefuk in thsi case
# Everytime you call dfs in the function call stack
# another layer is added with a different curr, so a different string
# that branch is going to see a different string

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        results = []

        def dfs(curr, open_left, close_left):

            if close_left < open_left or close_left < 0 or open_left < 0:
                return

            elif len(curr) == 2*n:
                results.append(curr)
                return

            else :
                dfs(curr + "(", open_left - 1, close_left)

                dfs(curr + ")", open_left, close_left - 1)


        dfs("", n, n)

        return results
        