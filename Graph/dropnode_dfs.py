class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = []


class Reorg:

    def height_after_drop(self, root, drop):

        if not root:
            return 0

        drop_set = set(drop)

        self.max_height = 0

        def dfs(node, parent_depth):

            if not node:
                return

            # 当前节点被删除，不增加高度
            if node.val in drop_set:
                cur_depth = parent_depth

            # 当前节点保留，占一层
            else:
                cur_depth = parent_depth + 1
                self.max_height = max(self.max_height, cur_depth)

            # 继续遍历所有孩子
            for child in node.next:
                dfs(child, cur_depth)

        dfs(root, 0)

        return self.max_height


if __name__ == "__main__":

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
    # 3

    print()

    print("Drop nothing")
    print(solver.height_after_drop(node1, []))
    # 4

    print()

    print("Drop 5")
    print(solver.height_after_drop(node1, [5]))
    # 3

    print()

    print("Drop 3 and 5")
    print(solver.height_after_drop(node1, [3, 5]))
    # 2