class MyQueue:

    def __init__(self):
        self.in_stack = [] # for write operation(push)
        self.out_stack = [] # for read operations(pead/pop)

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        # if out_stack is empty, transfer the queue in reverse order to out_stack(the queue is read from last of out_stack->front of in_stack)
        if self.out_stack:
            return self.out_stack.pop()
        else:
            while self.in_stack:
                val = self.in_stack.pop()
                self.out_stack.append(val)
            return self.out_stack.pop()

    def peek(self) -> int:
        if self.out_stack:
            return self.out_stack[-1]
        else:
            while self.in_stack:
                val = self.in_stack.pop()
                self.out_stack.append(val)
            return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()