class MinStack:

    def __init__(self):
        self.s = [] # stack struct: [val, currMinVal]

    def push(self, val: int) -> None:
        minVal = self.getMin()
        if minVal is None or val < minVal:
            minVal = val
        self.s.append([val, minVal])

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0] if self.s else None

    def getMin(self) -> int:
        return self.s[-1][1] if self.s else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()