from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size 
        self.arr = deque()
        self.summ = 0
        

    def next(self, val: int) -> float:
        if len(self.arr) == self.size:
            self.summ -= self.arr.popleft()
        
        self.arr.append(val)
        self.summ += val
        return self.summ / len(self.arr)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
