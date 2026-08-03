class MyHashSet:

    def __init__(self):
        self.size = 2069
        self.array = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.array[self.hashing(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.array[self.hashing(key)].remove(key)

    def contains(self, key: int) -> bool:
        for num in self.array[self.hashing(key)]:
            if num == key:
                return True
        return False

    def hashing(self, key):
        return key % self.size
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)