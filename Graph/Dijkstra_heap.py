import heapq

def dijkstra(graph, start):

    # shortest distance table
    # space: O(V)
    dist = {}

    # initialize all nodes
    # time: O(V)
    for node in graph:
        dist[node] = float('inf')

    # start node distance = 0
    # time: O(1)
    dist[start] = 0

    # min heap
    # stores: (distance, node)
    # space: O(E) worst case
    heap = []

    # initial push
    # time: O(1)
    heapq.heappush(heap, (0, start))

    # worst case:
    # heap may contain O(E) entries
    # because the same node can be pushed multiple times
    while heap:

        # pop current shortest distance node
        # time: O(log E)
        # usually written as O(log V)
        current_dist, u = heapq.heappop(heap)

        # outdated entry check (lazy deletion)
        # time: O(1)
        if current_dist > dist[u]:
            continue

        print(f"\nvisit: {u}")
        print("heap before:", heap)
        print("dist before:", dist)

        # iterate neighbors
        # total across whole algorithm:
        # O(E)
        for neighbor in graph[u]:

            # edge lookup
            # time: O(1)
            weight = graph[u][neighbor]

            # compute new distance
            # time: O(1)
            new_dist = dist[u] + weight

            # successful relaxation
            # time: O(1)
            if new_dist < dist[neighbor]:

                # update shortest distance
                # time: O(1)
                dist[neighbor] = new_dist

                # push updated distance into heap
                # each push: O(log E)
                # total pushes: at most O(E)
                heapq.heappush(
                    heap,
                    (new_dist, neighbor)
                )

        print("dist after :", dist)
        print("heap after :", heap)

    # return shortest distances
    # time: O(1)
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

# Final Time Complexity:
# O((V + E) log V)
# commonly simplified to:
# O(E log V)

# Space Complexity:
# dist  -> O(V)
# heap  -> O(E)
# total -> O(V + E)