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


# load inital risk level map
risk_levels = [[int(o) for o in line.strip()] for line in open("input.txt", "r")]

# created extended risk level map
extended_risk_levels = []
for j in range(5):
    for line in risk_levels:
        new_line = []
        for i in range(5):
            new_line.extend(
                list(
                    map(lambda x: (x + i + j) % 9 if (x + i + j) % 9 != 0 else 9, line)
                )
            )

        extended_risk_levels.append(new_line)


# build graph and init costs lkp
graph, costs, parents = {}, {}, {}

for y, line in enumerate(extended_risk_levels):
    for x, col in enumerate(line):
        neighbours = get_neighbours(extended_risk_levels, (x, y))
        graph[(x, y)] = {
            (nx, ny): extended_risk_levels[ny][nx] for (nx, ny) in neighbours
        }
        costs[(x, y)] = None


def search_dijkstra(graph, start, end):

    # cost, position in graph - this order is needed so that heapq will sort by the first element of the tuple
    queue = [(0, start)]
    print("TEST1")
    costs = defaultdict(lambda: inf, {start: 0})
    seen = set()
    print("TEST2")

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

            if new_cost < costs[neighbour]:
                costs[neighbour] = new_cost
                heapq.heappush(queue, (new_cost, neighbour))


start = (0, 0)
end = (len(extended_risk_levels[0]) - 1, len(extended_risk_levels) - 1)
target_cost = search_dijkstra(graph, start, end)

print(target_cost)


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

# creat extended risk level map
extended_risk_levels = []
for j in range(5):
    for line in risk_levels:
        new_line = []
        for i in range(5):
            new_line.extend(
                list(
                    map(lambda x: (x + i + j) % 9 if (x + i + j) % 9 != 0 else 9, line)
                )
            )

        extended_risk_levels.append(new_line)


# build graph and init costs lkp
graph = create_graph(risk_levels)

# find min cost for a path from the upper left corner (0,0) to lower right corner of the risk level map
start, end = (0, 0), (len(risk_levels[0]) - 1, len(risk_levels) - 1)
min_cost = search_dijkstra(graph, start, end)

print(min_cost)
