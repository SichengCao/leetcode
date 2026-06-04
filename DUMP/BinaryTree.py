from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val =val
        self.left = None
        self.right = None



def buildTree(arr):
        queue = deque()
        root = TreeNode(arr[0])
        queue.append(root)
        i = 1
        while queue and i < len(arr):
            node = queue.popleft()
            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)

            i+=1
            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i+=1
        return root


def printTreeByLevel(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        size = len(queue)  # 当前层的节点数
        level = []

        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print(level)

arr = [1,3,4,5,8,9]
tree = buildTree(arr)
printTreeByLevel(tree)

