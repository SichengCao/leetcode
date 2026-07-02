class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):

            pre = node.prev
            nex = node.next
            pre.next = nex
            nex.prev = pre

    def insertToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self,key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insertToHead(node)
        return node.val

    def put(self,key,value):

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insertToHead(node)
        else:
            node = Node(key,value)
            self.cache[key] = node
            self.insertToHead(node)

            if self.capacity < len(self.cache):
                node = self.tail.prev
                key = node.key
                self.remove(node)
                del self.cache[key]



