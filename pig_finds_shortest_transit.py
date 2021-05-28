from collections import deque, defaultdict


# Helper function
def construct_graph(routes):
    G = defaultdict(set)
    for name in routes:
        for ix, stop_name in enumerate(routes[name]):
            G[stop_name] = G[stop_name].union(set(routes[name][ix + 1 :]))
    return G


# Method: BFS
def find_least_transit(routes_map, start, end):
    G = construct_graph(routes_map)
    Q = deque()
    visited = set()
    Q.append((start, 0))
    visited.add(start)
    while len(Q) > 0:
        stop, steps = Q.popleft()
        if stop == end:
            return steps
        for next_stop in G[stop]:
            if next_stop not in visited:
                visited.add(next_stop)
                Q.append((next_stop, steps + 1))
    return -1


routes_map = {
    "yonge": ["A", "B", "C", "D", "E"],
    "bay": ["C", "D", "G", "Y", "K"],
    "dundas": ["I", "O", "K", "G", "F"],
    "king": ["K", "F", "M", "N"],
}


# 0
print(find_least_transit(routes_map, "A", "A"))

# 1
print(find_least_transit(routes_map, "A", "C"))

# 3
print(find_least_transit(routes_map, "A", "M"))

# -1
print(find_least_transit(routes_map, "B", "I"))
