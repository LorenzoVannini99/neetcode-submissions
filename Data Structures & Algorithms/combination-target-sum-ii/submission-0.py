class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # Quite similar to combination sum 1
        # The problem is we have to keep track how many time swe have chosen something

        res = []
        subset = []
        candidates.sort()

        def dfs(i, summation):
            # If exact target reached → store a copy of the subset
            if summation == target:
                res.append(subset.copy())
                return
            
            # If we exceeded the target or reached end of list → stop exploring
            if summation > target or i == len(candidates):
                return

            # 1. Include current candidate
            subset.append(candidates[i])
            dfs(i + 1, summation + candidates[i])
            subset.pop()

            # 2. Skip current candidate (and all its duplicates)
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, summation)

        dfs(0, 0)
        return res
