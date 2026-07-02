class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class WaitList:

    def __init__(self):
        self.map = {}
        self.head = Node("",None)
        self.tail = Node("", None)

        self.head.next = self.tail
        self.tail.prev = self.head


    def add_seat(self,name,size):

        node = Node(name,size)
        map[name] = node

        prev_tail = self.tail.prev
        prev_tail.next = node

        node.prev = prev_tail
        node.next =self.tail
        self.tail.prev = node

        self.map[name] = node


    def remove_party(self,name):

        if name not in self.map:
            return False

        node = self.map[name]

        prev_node = node.prev
        next_node = node.next
        