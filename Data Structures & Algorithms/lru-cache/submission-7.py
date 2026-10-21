class LRUCache:

    def __init__(self, capacity: int):
        self.lcache = {}
        self.llist = LinkedList()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.lcache:
            node = self.lcache[key]
            self.llist.delete(node)
            node = self.llist.insert(key,node.value)
            self.lcache[key] = node
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lcache:
            node = self.lcache[key]
            self.llist.delete(node)
            n = self.llist.insert(key,value)
            self.lcache[key] = n
        else:
            node = self.llist.insert(key,value)
            if self.llist.size > self.capacity:
                tail = self.llist.tail
                self.llist.delete(tail)
                self.lcache.pop(tail.key)
            self.lcache[key] = node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def insert(self,key,value):
        node = Node(key,value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size+=1
        return node
    def delete(self, node):
        left, right = node.prev, node.next
        node.next = None
        node.prev = None
        if left:
            left.next = right
        else:
            self.head = right
        if right:
            right.prev = left
        else:
            self.tail = left
        self.size -= 1



class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None