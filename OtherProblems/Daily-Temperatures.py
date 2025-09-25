class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while s and temperatures[s[-1]] <= temperatures[i]:
                s.pop()
            res[i] = s[-1] - i if s else 0
            s.append(i)
        return res
