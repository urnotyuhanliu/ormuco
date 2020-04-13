import collections

class LRUCache:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache: #expire reture -1
            return -1
        value = self.cache.pop(key) 
        self.cache[key] = value   # set key as the newest one
        return value

    def put(self, key, value):
        if key in self.cache:    
            self.cache.pop(key)
        elif len(self.cache) == self.capacity: 
            self.cache.popitem(last=False)  #is full
        self.cache[key] = value
        
cache = LRUCache(4)
cache.put(1,1)
cache.put(2,3)
cache.put(3,5)
cache.get(2)
cache.put(4,8)
cache.get(4)
cache.put(5,2)
cache.get(5)
cache.get(1) 