from collections import deque
from math import prod


# find valid neighbours (their x,y position)
def get_neighbours(grid, node):
    terms = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x_size, y_size = len(grid[0]) - 1, len(grid) - 1

    x, y = node
    for (tx, ty) in terms:
        if 0 <= x + tx <= x_size and 0 <= y + ty <= y_size:
            yield (x + tx, y + ty)


# do a classic bfs assume 9 is a wall/cannot be visited
def bfs(graph, root):
    seen, queue = set([root]), deque([root])

    while queue:
        node = queue.popleft()
        for (nx, ny) in list(get_neighbours(graph, node)):
            if (nx, ny) not in seen and int(graph[ny][nx]) != 9:
                seen.add((nx, ny))
                queue.append((nx, ny))

    return seen


heightmap = [line.strip() for line in open("input.txt", "r")]
basins = []

for y, line in enumerate(heightmap):
    for x, loc in enumerate(line):
        loc_value = int(loc)
        neighbours = get_neighbours(heightmap, (x, y))

        # check if lower locations exist
        le_points = [True for (nx, ny) in neighbours if int(heightmap[ny][nx]) <= loc_value]

        # current point is the lowest point
        if not le_points:
            basin = bfs(heightmap, (x, y))
            basin_size = len(basin)

            basins.append(basin_size)


print(prod(sorted(basins, reverse=True)[:3]))
