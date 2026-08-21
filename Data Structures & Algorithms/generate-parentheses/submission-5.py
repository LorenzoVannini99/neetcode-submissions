class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        results = []

        def dfs(curr, open_left, close_left):

            if close_left < open_left or close_left < 0 or open_left < 0:
                return
            if len(curr) == 2*n:
                results.append(curr)
                return

            dfs(curr + "(", open_left - 1, close_left)

            dfs(curr + ")", open_left, close_left - 1)


        dfs("", n, n)

        return results
        