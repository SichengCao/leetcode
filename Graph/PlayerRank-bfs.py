from collections import defaultdict, deque


def preciseRanks(n, matches):

    # winner -> loser
    graph = defaultdict(list)

    # loser -> winner
    reverse_graph = defaultdict(list)

    for winner, loser in matches:

        graph[winner].append(loser)

        reverse_graph[loser].append(winner)

    print("Graph: " , graph)
    print("Reverse_Graph: ", reverse_graph)

    # count how many nodes are reachable
    def bfs(start, g):

        visited = set()

        queue = deque([start])

        while queue:

            node = queue.popleft()

            for nei in g[node]:

                if nei not in visited:

                    visited.add(nei)

                    queue.append(nei)

        return len(visited)

    result = []

    for player in range(1, n + 1):

        # players I can beat
        win_count = bfs(player, graph)

        # players who can beat me
        lose_count = bfs(player, reverse_graph)

        # rank uniquely determined
        if win_count + lose_count == n - 1:

            rank = lose_count + 1

            result.append((player, rank))

    return result


# -------------------
# Example
# -------------------

n = 5

matches = [
    (4, 3),
    (4, 2),
    (3, 2),
    (1, 2),
    (2, 5)
]

print(preciseRanks(n, matches))