from collections import deque


def find_panda_root(graph, colors):

    n = len(graph)

    # -----------------------------------
    # Step 1:
    # BFS to compute depth parity
    # -----------------------------------

    depth = [-1] * n

    queue = deque([0])

    depth[0] = 0

    while queue:

        node = queue.popleft()

        for nei in graph[node]:

            if depth[nei] == -1:

                depth[nei] = depth[node] + 1

                queue.append(nei)

    # -----------------------------------
    # Step 2:
    # Check panda coloring
    #
    # Pattern 1:
    # even depth = B
    # odd depth  = W
    #
    # Pattern 2:
    # even depth = W
    # odd depth  = B
    # -----------------------------------

    def valid(start_color):

        for node in range(n):

            # expected color for this node

            if depth[node] % 2 == 0:

                expected = start_color

            else:

                expected = 'W' if start_color == 'B' else 'B'

            # mismatch
            if colors[node] != expected:
                return False

        return True

    # if neither pattern works
    if not valid('B') and not valid('W'):
        return -1

    # -----------------------------------
    # Step 3:
    # Find valid binary tree root
    #
    # root can have at most 2 children
    # -----------------------------------

    for node in range(n):

        if len(graph[node]) <= 2:
            return node

    return -1


# ------------------------------------------------
# Example
# ------------------------------------------------

graph = [
    [1],
    [0, 2, 3],
    [1],
    [1, 4],
    [3]
]

colors = ['B', 'W', 'B', 'B', 'W']

ans = find_panda_root(graph, colors)

print("Valid Panda Tree Root =", ans)