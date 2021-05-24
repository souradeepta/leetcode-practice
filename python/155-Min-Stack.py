class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minEle = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minEle or x <= self.minEle[-1]:
            self.minEle.append(x)

    def pop(self) -> None:
        m = self.stack.pop()
        if m == self.minEle[-1]:
            self.minEle.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minEle:
            return self.minEle[-1]
        return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_2 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(f'{param_2}, {param_3}, {param_4}')
