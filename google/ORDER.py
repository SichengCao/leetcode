class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        # hashmap: value -> node
        self.map = {}

    def insert_sorted(self, val):

        # avoid duplicates
        if val in self.map:
            return

        new_node = Node(val)
        self.map[val] = new_node

        curr = self.head.next

        # O(n) traversal to find insertion position
        while curr != self.tail and curr.val < val:
            curr = curr.next

        prev_node = curr.prev

        # insert between prev_node and curr
        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = curr
        curr.prev = new_node

    def remove(self, val):

        if val not in self.map:
            return

        node = self.map[val]

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        del self.map[val]

    def print_list(self):

        curr = self.head.next

        while curr != self.tail:
            print(curr.val, end=" ")

            curr = curr.next

        print()


# =========================
# main function
# =========================

if __name__ == "__main__":

    ordered = OrderedList()

    print("Insert values:")

    ordered.insert_sorted(10)
    ordered.insert_sorted(5)
    ordered.insert_sorted(20)
    ordered.insert_sorted(15)
    ordered.insert_sorted(8)

    ordered.print_list()

    print("\nRemove 10:")
    ordered.remove(10)
    ordered.print_list()

    print("\nInsert 7:")
    ordered.insert_sorted(7)
    ordered.print_list()