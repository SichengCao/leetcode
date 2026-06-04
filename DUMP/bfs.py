from collections import deque

def bfs(start, graph):

    queue = deque([start])
    visited = set([start])

    while queue:

        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs('A', graph)