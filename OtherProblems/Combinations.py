class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking(curr, j):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(j, n):
                curr.append(i+1)
                backtracking(curr, i+1)
                curr.pop()
            return

        backtracking([], 0)
        return res