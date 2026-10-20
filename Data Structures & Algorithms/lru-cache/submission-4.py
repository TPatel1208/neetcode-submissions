class LRUCache:

    def __init__(self, capacity: int):
        self.lruCache = {}
        self.ll = LinkedList()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key in self.lruCache:
            node = self.lruCache[key]
            self.ll.delete(node)
            self.ll.insert(node)
            return node.value
            
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key,value)
        if key in self.lruCache:
            self.ll.delete(self.lruCache[key])
            self.ll.insert(node)
            self.lruCache[key] = node
        else:
            self.ll.insert(node)
            self.lruCache[key] = node
            if self.ll.size > self.capacity:
                lru_node = self.ll.tail
                self.ll.delete(lru_node)
                self.lruCache.pop(lru_node.key)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def insert(self,node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size +=1
    def delete(self,node):
        n = node.next
        p = node.prev

        if node.prev:
            p.next = n
        if node.next:
            n.prev = p
        if node == self.tail:
            self.tail = p
        if node == self.head:
            self.head = n
        node.next = None
        node.prev = None
        self.size -=1
        
            


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
