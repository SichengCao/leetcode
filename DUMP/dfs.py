def dfs(node, graph, visited):
    if node in visited:
        print(node + "has been visted")
        return

    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        dfs(neighbor, graph, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E','A'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()

dfs('A', graph, visited)