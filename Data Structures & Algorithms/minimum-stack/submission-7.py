class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.min_stack.append(min(val, self.min_stack[-1] if self.stack else val))
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        else:
            raise ValueError("Stack is empty")
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            raise ValueError("Stack is empty!")
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
