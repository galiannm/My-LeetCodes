class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for op in operations:
            if op == '+':
                s.append(s[-2] + s[-1]) 
            elif op == 'D':
                s.append(s[-1]*2) 
            elif op == 'C':
                s.pop()
            else:
                s.append(int(op))
        return sum(s)