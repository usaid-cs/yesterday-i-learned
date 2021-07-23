class MinStack:
    stack = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(0)

    def top(self) -> int:
        if self.stack:
            return self.stack[0]
        return -1

    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
