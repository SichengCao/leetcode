from collections import deque


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = []


class Reorg:

    def height_after_drop(self, root, drop):
        if not root:
            return 0

        # drop = [3,5]  -> {3,5}
        drop_set = set(drop)

        # (node, parent_depth)
        queue = deque()
        queue.append((root, 0))

        max_height = 0

        while queue:

            node, parent_depth = queue.popleft()

            # 当前节点被删除，不增加高度
            if node.val in drop_set:
                cur_depth = parent_depth

            # 当前节点保留，占一层
            else:
                cur_depth = parent_depth + 1
                max_height = max(max_height, cur_depth)

            # 所有孩子继续向下
            for child in node.next:
                queue.append((child, cur_depth))

        return max_height


if __name__ == "__main__":

    # 建树
    #
    #        1
    #       / \
    #      2   3
    #         / \
    #        4   5
    #             |
    #             6
    #

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = [node2, node3]
    node3.next = [node4, node5]
    node5.next = [node6]

    solver = Reorg()

    print("Drop 3")
    print(solver.height_after_drop(node1, [3]))
    # Expected: 3

    print()

    print("Drop nothing")
    print(solver.height_after_drop(node1, []))
    # Expected: 4

    print()

    print("Drop 5")
    print(solver.height_after_drop(node1, [5]))
    # Expected: 3

    print()

    print("Drop 3 and 5")
    print(solver.height_after_drop(node1, [3, 5]))
    # Expected: 2