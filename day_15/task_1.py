from math import inf
from collections import defaultdict
import heapq

# find valid neighbours (their x,y position)
def get_neighbours(grid, node):
    terms = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    x_size, y_size = len(grid[0]) - 1, len(grid) - 1

    x, y = node
    for (tx, ty) in terms:
        if 0 <= x + tx <= x_size and 0 <= y + ty <= y_size:
            yield (x + tx, y + ty)


def create_graph(risk_levels):
    graph = {}

    for y, line in enumerate(risk_levels):
        for x, col in enumerate(line):
            neighbours = get_neighbours(risk_levels, (x, y))
            graph[(x, y)] = {(nx, ny): risk_levels[ny][nx] for (nx, ny) in neighbours}

    return graph


def search_dijkstra(graph, start, end):

    # (cost, position in graph) - this order is needed so that heapq will sort by the first element of the tuple
    queue = [(0, start)]
    costs = defaultdict(lambda: inf, {start: 0})
    seen = set()

    while queue:
        # heapq - The smallest element has the highest priority
        # heapq insert is O(log n) which beats O(n) for a sorted list
        cost, node = heapq.heappop(queue)  # gets the smallest element

        if node == end:
            return cost

        if node in seen:
            continue

        seen.add(node)

        for neighbour in graph[node]:
            new_cost = cost + graph[node][neighbour]

            # update neighbour cost if cost of the current path is smaller than the cost currently stored
            if new_cost < costs[neighbour]:
                costs[neighbour] = new_cost
                heapq.heappush(queue, (new_cost, neighbour))


# load inital risk level map
risk_levels = [[int(o) for o in line.strip()] for line in open("input.txt", "r")]

# build graph and init costs lkp
graph = create_graph(risk_levels)

# find min cost from upper left corner (0,0) to lower right corner of the risk level map
start, end = (0, 0), (len(risk_levels[0]) - 1, len(risk_levels) - 1)
min_cost = search_dijkstra(graph, start, end)

print(min_cost)
