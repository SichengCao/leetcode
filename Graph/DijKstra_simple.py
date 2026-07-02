import heapq


def dijkstra(graph, start):

    dist = {}
    visited = {}

    # 初始化
    for node in graph:
        dist[node] = float('inf')
        visited[node] = False

    dist[start] = 0

    print(dist)

    for _ in range(len(graph)):

        u = None

        for node in graph:

            if not visited[node]:

                if u is None or dist[node] < dist[u]:
                    u = node
        visited[u] = True

        print(f"\nvisit: {u}")
        print("dist before:", dist)

        for neighbor in graph[u]:

            weight = graph[u][neighbor]

            if dist[u] + weight < dist[neighbor]:
                dist[neighbor] = dist[u] + weight

        print("dist after : ", dist)

    return dist


graph = {
    'a': {
        'b': 2,
        'c': 5
    },

    'b': {
        'c': 1,
        'd': 3
    },

    'c': {
        'd': 3,
        'e': 4,
        'f': 1
    },

    'd': {
        'e': 1,
        'f': 4
    },

    'e': {
        'f': 1
    },

    'f': {}
}

print(dijkstra(graph, 'a'))