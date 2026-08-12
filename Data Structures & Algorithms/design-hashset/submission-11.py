class MyHashSet:

    def __init__(self):
        self.size = 2069
        self.arr = [[] for _ in range(self.size)]
        

    def add(self, key: int) -> None:
        bucket_index = self.__calculate_hash(key)
        if not key in self.arr[bucket_index]:
            self.arr[self.__calculate_hash(key)].append(key)
        

    def remove(self, key: int) -> None:
        bucket_index = self.__calculate_hash(key)
        if key in self.arr[bucket_index]:
            self.arr[self.__calculate_hash(key)].remove(key)
        

    def contains(self, key: int) -> bool:
        bucket_index = self.__calculate_hash(key)
        return key in self.arr[bucket_index]


    def __calculate_hash(self, key: int) -> int:
        return key % self.size
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)