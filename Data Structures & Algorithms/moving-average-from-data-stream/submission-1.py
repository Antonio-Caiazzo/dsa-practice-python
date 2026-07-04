from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size 
        self.arr = deque()
        self.summ = 0
        self.l = 0
        

    def next(self, val: int) -> float:
        self.l += 1
        if self.l > self.size:
            self.summ -= self.arr.popleft()
            self.l -= 1
        
        self.arr.append(val)
        self.summ += val
        return self.summ / self.l
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
