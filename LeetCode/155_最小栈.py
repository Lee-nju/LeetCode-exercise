class MinStack:
    """最小栈：能在常数时间内检索到最小元素的栈"""

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 栈里面的每个元素存储:[值，当前位置到栈底的最小值]
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack or self.stack[-1][1] >= x:
            self.stack.append([x, x])
        else:
            self.stack.append([x, self.stack[-1][1]])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
