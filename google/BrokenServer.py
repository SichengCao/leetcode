from collections import deque

def minTeleportations(connections, broken, start, end):

        queue = deque()
        queue.append((start,0))

        visited = set()
        visited.add(start)

        while queue:
            node, steps = queue.popleft()

            if node == end:
                return steps

            for nei in connections[node]:
                if nei in broken:
                    continue
                if nei in visited:
                    continue

                visited.add(nei)
                queue.append((nei,steps+1))

        return -1



connections = {
    0: [1],
    1: [2,5],
    2:[1,3,4,5],
    3:[1,2,5],
    4:[2,5],
    5:[1,2,3,4]

}

broken = {5}

start = 0
end = 4

print(minTeleportations(connections,broken,start,end))