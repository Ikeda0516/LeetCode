class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.arr = []
        
    def get(self, key):
        if key in self.arr:
            i = self.arr.index(key)
            self.arr.pop(i)
            self.arr.append(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.arr:
            i = self.arr.index(key)
            self.arr.pop(i)
        else:
            if len(self.arr) >= self.capacity:
                self.arr.pop(0)
        self.arr.append(key)
        self.dic[key] = value