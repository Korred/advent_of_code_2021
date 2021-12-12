from collections import deque, defaultdict

with open("test_input.txt", "r") as connections:
    edges = defaultdict(list)
    
    for c in connections:
        (v1, v2) = c.strip().split("-")
        
        edges[v1].append(v2)
        
        # edge reversal doesnt matter for start and end, since those nodes can only be visted once
        if v2 != "end" and v1 != "start":
            edges[v2].append(v1)


# bfs but start/end/smaller caves can only be visted once
# each path starts with "start" and ends with "end" vertex/node
def find_distinct_paths(edges):
    
    seen, queue = set([root]), deque([root])

    while queue:
        node = queue.popleft()
        for (nx, ny) in list(get_neighbours(graph, node)):
            if (nx, ny) not in seen and int(graph[ny][nx]) != 9:
                seen.add((nx, ny))
                queue.append((nx, ny))

    return seen