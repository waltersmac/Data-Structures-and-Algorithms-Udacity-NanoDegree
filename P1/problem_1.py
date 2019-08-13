from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache
        if key in self.cache:
            self.cache.pop(key)
        
        self.cache[key] = value
        
        # If the cache is at capacity remove the oldest item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
        
cache = LRU_Cache(5)

cache.set(1, 1);
cache.set(2, 2);
cache.set(3, 3);
cache.set(4, 4);


print(cache.get(1))       # returns 1
print(cache.get(2))       # returns 2
print(cache.get(9))      # returns -1 because 9 is not present in the cache

cache.set(5, 5) 
cache.set(6, 6)

print(cache.get(3))      # returns -1 because the cache reached it's capacity 
                         # and 3 was the least recently used entry


cache.set(4, 4)        # Set same number
print(cache.get(4))    # returns 4 as same number is still there