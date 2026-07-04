from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()
        self.size = 0


    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1
        

    def pop(self) -> int:
        if self.empty():
            raise Exception("The stack is empty")
        self.size -= 1
        for _ in range(self.size):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()
        
        

    def top(self) -> int:
        if self.empty():
            raise Exception("The stack is empty")
        return self.queue[-1]


    def empty(self) -> bool:
        return self.size == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()