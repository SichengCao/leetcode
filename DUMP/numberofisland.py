def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])

    # main function for recursion the island
    def dfs(r, c):
        # if reach the wall
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        # if reach the sea
        if grid[r][c] == '0':
            return
        # mark the current node as visited by turning it into ocean
        grid[r][c] = '0'

        # recursively flood to every direction
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0

    for r in range(rows):
        for c in range(cols):
            # find any point which represents islands
            # find everything connected with that point and turn those into vistied
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count


grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

print(numIslands(grid))
