from collections import deque, defaultdict

with open("input.txt", "r") as connections:
    edges = defaultdict(list)

    for c in connections:
        (v1, v2) = c.strip().split("-")
        edges[v1].append(v2)
        edges[v2].append(v1)


# bfs - start/end/smaller caves can only be visted once
# each path starts with "start" and ends with "end" vertex/node
def find_distinct_paths(edges):

    paths = deque([["start"]])
    completed_paths = []

    while paths:
        path = paths.popleft()

        s_node = path[-1]
        e_nodes = edges[s_node]

        for node in e_nodes:
            if node == "end":
                completed_paths.append(path + [node])
                continue

            if node == "start":
                continue

            if node.islower():
                # check if node was already visited
                if node in path:
                    continue

            paths.append(path + [node])

    return completed_paths


print(len(find_distinct_paths(edges)))
