from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        # initializing capacity and using ordered dict to 
        # maintain order of insertion, cache functionality
        self.cap = capacity
        self.lru = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lru:
            # using the move_to_end method from ordered dict,
            # which removes the key from place and reinserts
            self.lru.move_to_end(key)
            return self.lru[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # removing oldest object in cache if it is full
        if key not in self.lru and len(self.lru) == self.cap:
            self.lru.popitem(last = False)
        # adding object to ordered dict cache 
        self.lru[key] = value
        self.lru.move_to_end(key)
