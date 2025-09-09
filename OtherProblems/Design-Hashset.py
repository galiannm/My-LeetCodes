class MyHashSet:

    def __init__(self):
        self.set = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        cur = self.hash(key)
        if key not in self.set[cur]:
            self.set[cur].append(key)
        

    def remove(self, key: int) -> None:
        cur = self.hash(key)
        if key in self.set[cur]:
            self.set[cur].remove(key)

    def contains(self, key: int) -> bool:
        cur = self.hash(key)
        return key in self.set[cur]

    def hash(self, key):
        return key % len(self.set)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)