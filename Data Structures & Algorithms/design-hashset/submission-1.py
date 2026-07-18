class MyHashSet:

    def __init__(self):
        self.size = 10**5
        self.bucket = [[] for _ in range(self.size)]
        
    def add(self, key: int) -> None:
        if self.contains(key):
            return 
        idx = key % 10**5
        self.bucket[idx].append(key)

        

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return 
        idx = key % 10**5
        self.bucket[idx].remove(key)
        

    def contains(self, key: int) -> bool:
        idx = key % 10**5
        values = self.bucket[idx]
        for value in values:
            if value == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)