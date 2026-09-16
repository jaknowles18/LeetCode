class MyQueue:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.length = self.length + 1
        

    def pop(self) -> int:
        
        if self.length == 0:
            return -1
        
        element = self.stack[0]

        for i in range(0, self.length - 1):
            self.stack[i] = self.stack[i + 1]

        self.length = self.length - 1
        self.stack.pop()
        return element

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return self.length == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()