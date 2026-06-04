from collections import deque


def zeroOneBFS(graph, start):

    # dist = {}
    #
    # for node in graph:
    #     dist[node] = float('inf')
    #
    # dist[start] = 0
    #
    # dq = deque([start])
    #
    # while dq:
    #
    #     node = dq.popleft()
    #
    #     for nei, weight in graph[node]:
    #
    #         newDist = dist[node] + weight
    #
    #         if newDist < dist[nei]:
    #
    #             dist[nei] = newDist
    #
    #             # weight = 0
    #             if weight == 0:
    #                 dq.appendleft(nei)
    #
    #             # weight = 1
    #             else:
    #                 dq.append(nei)
    #
    # return dist

    dist = {}
    for node in graph:
        dist[node] = float('inf')

    dist[start] = 0
    dq = deque([start])

    while dq:
        node = dq.popleft()

        for nei, weight in graph[node]:
            newDist = dist[node] + weight
            if newDist < dist[nei]:
                dist[nei] = newDist

                if weight == 0:
                    dq.appendleft(nei)
                else:
                    dq.append(nei)

    return dist
graph = {
    1: [(2, 0), (3, 1)],
    2: [(4, 1)],
    3: [(4, 0)],
    4: []
}

print(zeroOneBFS(graph, 1))