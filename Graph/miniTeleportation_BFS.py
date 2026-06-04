from collections import deque


def minTeleportations(connections, broken, start, end):

    # queue = deque()
    # queue.append((start,0))
    #
    # visited = set()
    # visited.add(start)
    #
    # while queue:
    #
    #     node,steps = queue.popleft()
    #     if node == end:
    #         return steps
    #
    #     for nei in connections[node]:
    #         if nei in broken or nei in visited:
    #             continue
    #         visited.add(nei)
    #         queue.append((nei,steps+1))
    #
    # return -1

    queue = deque()
    queue.append((start,0))
    visited = set()
    visited.add(start)

    while queue:
        node, steps = queue.popleft()
        if node == end:
            return steps
        for nei in connections[node]:
            if nei in broken or nei in visited:
                continue
            else:
                visited.add(nei)
                queue.append((nei,steps+1))

    return -1


connections = {
    0: [6],
    1: [2, 5],
    2: [1, 3, 4, 5],
    3: [1, 4, 5],
    4: [6],
    5: [6],
    6: []
}

broken = set([5])

print(minTeleportations(connections, broken, 1, 3))