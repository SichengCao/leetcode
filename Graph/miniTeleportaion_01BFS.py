from collections import deque


def minBrokenTeleporters01BFS(
    connections,
    broken,
    start,
    end
):

    broken = set(broken)

    INF = float('inf')

    # shortest distance
    dist = {}

    for node in connections:
        dist[node] = INF

    dist[start] = 0

    dq = deque()
    dq.append(start)

    print("Initial State")
    print("deque:", list(dq))
    print("dist :", dist)
    print()

    while dq:

        node = dq.popleft()

        print("===================================")
        print("POP NODE:", node)
        print("Current deque:", list(dq))
        print("Current dist :", dist)
        print()

        # reached destination
        if node == end:
            print("Reached destination!")
            return dist[node]

        for nei in connections[node]:

            # binary weight
            cost = 1 if nei in broken else 0

            newDist = dist[node] + cost

            print(f"Check neighbor {nei}")
            print("cost =", cost)
            print("newDist =", newDist)
            print("oldDist =", dist[nei])

            # relax edge
            if newDist < dist[nei]:

                print("UPDATE distance!")

                dist[nei] = newDist

                # cost 0:
                # process earlier
                if cost == 0:

                    dq.appendleft(nei)

                    print(f"appendleft({nei})")

                # cost 1:
                # process later
                else:

                    dq.append(nei)

                    print(f"append({nei})")

            else:
                print("No update")

            print("deque now:", list(dq))
            print("dist now :", dist)
            print()

    return -1


connections = {
    1: [2, 3],
    2: [4],
    3: [5],
    5: [4],
    4: []
}

broken = set([2])

start = 1
end = 4

result = minBrokenTeleporters01BFS(
    connections,
    broken,
    start,
    end
)

print()
print("FINAL ANSWER =", result)