import heapq as hq

# Helper function
def hit_wall(grid, cur, direction):
    # Return position pig hits wall if she goes in given direction,
    # or (None, None) if she cannot go in that direction
    row, col = cur
    while True:
        nr = row + direction[0]
        nc = col + direction[1]
        if (
            nr < 0
            or nr >= len(grid)
            or nc < 0
            or nc >= len(grid[0])
            or grid[nr][nc] == "#"
            or grid[row][col] == "9"
        ):
            break
        row = nr
        col = nc
    if row != cur[0] or col != cur[1]:
        return (row, col)
    else:
        return (None, None)


# Helper function
def neighbors(grid, cur):
    # Cur is position, eg (2, 0)
    # Return list of squares you can get to in one turn, and their distance
    # eg: [((2, 1), 1), ((3, 0), 1)]
    ans = []
    for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = hit_wall(grid, cur, direction)
        if nr is not None:
            ans.append(((nr, nc), abs(cur[0] - nr) + abs(cur[1] - nc)))
    return ans


# Method: Dijkstra
def dijkstra(grid):
    R = len(grid)
    C = len(grid[0])
    visited = set()
    start, goal = None, None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "1":
                start = (r, c)
            if grid[r][c] == "9":
                goal = (r, c)

    Q = []
    hq.heappush(Q, (0, start))
    while len(Q) > 0:
        curdist, curnode = hq.heappop(Q)
        visited.add(curnode)
        if curnode == goal:
            return curdist
        for nei, ndist in neighbors(grid, curnode):
            if nei not in visited:
                hq.heappush(Q, (curdist + ndist, nei))
    return -1


grid1 = [["9", ".", "#"], ["#", ".", "."], [".", "#", "."], ["1", ".", "."]]

# 7
print(dijkstra(grid1))


grid2 = [[".", ".", "."], ["#", "9", "."], [".", "#", "."], ["1", ".", "."]]

# -1
print(dijkstra(grid2))


grid3 = [["#", ".", "#"], [".", "9", "."], [".", "#", "."], ["1", ".", "."]]

# 3
print(dijkstra(grid3))
