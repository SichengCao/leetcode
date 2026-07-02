def is_tree(parent):
    n = len(parent)

    # 1. 必须只有一个 root
    roots = 0

    for p in parent:
        if p == -1:
            roots += 1

    if roots != 1:
        return False

    # 2. parent index 必须合法
    for i in range(n):
        p = parent[i]

        if p != -1:
            if p < 0 or p >= n:
                return False

            if p == i:
                return False

    # 3. DFS 染色检测 cycle
    state = [0] * n
    # 0 = unvisited
    # 1 = visiting
    # 2 = visited

    def dfs(node):

        if state[node] == 1:
            return False

        if state[node] == 2:
            return True

        state[node] = 1

        p = parent[node]

        if p != -1:
            if not dfs(p):
                return False

        state[node] = 2

        return True

    for i in range(n):
        if not dfs(i):
            return False

    return True