class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.ll = linkedList()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            v = n.value
            self.ll.delete(n)
            self.cache[key] = self.ll.insert(key,v)
            
            return v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            n = self.cache[key]
            self.ll.delete(n)
            i = self.ll.insert(key,value)
            self.cache[key]=i
        else:
            i = self.ll.insert(key,value)
            self.cache[key]=i
            if self.ll.size>self.capacity:
                head = self.ll.root
                self.cache.pop(head.key)
                self.ll.delete(head)
                

class node:
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class linkedList:
    def __init__(self):
        self.root = None
        self.end = None
        self.size = 0
    def insert(self, key,value):
        n = node(key,value)
        if self.root is None:
            self.root = n
            self.end = n
            self.size +=1
        else:
            n.prev = self.end
            self.end.next = n
            self.end = n
            self.size +=1
        return n
    def delete(self,node):
        e = node.next
        p = node.prev

        if e is not None:
            e.prev = p
        if p is not None:
            p.next = e
        if node == self.root:
            self.root = e
        if node == self.end:
            self.end = p
        self.size -=1        
            

