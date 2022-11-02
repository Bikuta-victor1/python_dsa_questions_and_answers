
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache.
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

class Node:   
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = self.prev = None

        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache ={}
        self.right, self.left = Node(0,0), Node(0,0)
        self.right.prev, self.left.next = self.left, self.right
        
    def remove(self, node):
        nxt, prev = node.next , node.prev
        nxt.prev, prev.next = prev, nxt
        
    def insert(self, node):
        nxt, prev = self.right, self.right.prev
        nxt.prev = prev.next = node
        node.next, node.prev = nxt, prev      
        
    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
        self.cache[key]  = Node(key, value)
        self.insert(self.cache[key])
        
        if self.cap < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)