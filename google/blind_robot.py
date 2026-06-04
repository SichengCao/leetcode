from collections import deque

# -----------------------------------
# directions
# -----------------------------------

DIRS = [
    (1, 0, 'D'),
    (-1, 0, 'U'),
    (0, 1, 'R'),
    (0, -1, 'L')
]


def escape_maze(grid):

    rows = len(grid)
    cols = len(grid[0])

    # -----------------------------------
    # find exit
    # -----------------------------------

    exit_x = exit_y = -1

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 'E':
                exit_x = i
                exit_y = j

    # -----------------------------------
    # BFS:
    # from one start -> exit
    # -----------------------------------

    def bfs(start_x, start_y):

        q = deque()
        q.append((start_x, start_y))

        visited = set()
        visited.add((start_x, start_y))

        # child -> parent
        parent = {}

        while q:

            x, y = q.popleft()

            # found exit
            if (x, y) == (exit_x, exit_y):
                break

            for dx, dy, move in DIRS:

                nx = x + dx
                ny = y + dy

                # boundary
                if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                    continue

                # wall
                if grid[nx][ny] == '#':
                    continue

                if (nx, ny) in visited:
                    continue

                visited.add((nx, ny))

                # store parent
                parent[(nx, ny)] = (x, y, move)

                q.append((nx, ny))

        # -----------------------------------
        # reconstruct path
        # -----------------------------------
        print(parent)
        path = []

        cur = (exit_x, exit_y)

        while cur != (start_x, start_y):

            px, py, move = parent[cur]

            path.append(move)

            cur = (px, py)

        path.reverse()

        return ''.join(path)

    # -----------------------------------
    # final answer
    # -----------------------------------

    answer = []

    for i in range(rows):
        for j in range(cols):

            # skip walls
            if grid[i][j] == '#':
                continue

            # skip exit itself
            if grid[i][j] == 'E':
                continue

            path = bfs(i, j)

            print(f"start = ({i},{j}) -> path = {path}")

            answer.append(path)

    return ''.join(answer)


# -----------------------------------
# sample input
# -----------------------------------

grid = [
    "#######",
    "#..#..#",
    "#..#E.#",
    "#.....#",
    "#######"
]

# -----------------------------------
# run
# -----------------------------------

res = escape_maze(grid)

print("\nFinal Command Sequence:")
print(res)