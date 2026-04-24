class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Brute force solution
        t = temperatures

        res = [0] * len(t)

        for i in range(len(t)):
            for j in range(i + 1, len(t)):
                if t[j] > t[i]:
                    res[i] = j - i
                    break
                

        return res



        








        