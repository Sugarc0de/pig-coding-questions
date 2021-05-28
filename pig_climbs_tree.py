from collections import defaultdict

# Method: DFS
def num_ways_to_climb(tree, target):
    D = defaultdict(set)
    for start, end, dist in tree:
        D[start].add((end, dist))
    ans = 0

    def dfs(node, sofar):
        nonlocal ans
        if sofar > target:
            return
        if len(D[node]) == 0:
            if sofar <= target:
                ans += 1
        for neighbor, dist in D[node]:
            dfs(neighbor, sofar + dist)

    children = set([end for _, end, _ in tree])
    start = None
    for k in D.keys():
        if k not in children:
            start = k
            break
    dfs(start, 0)
    return ans


tree = [
    ("A", "B", 3),
    ("A", "C", 1),
    ("B", "D", 6),
    ("B", "E", 1),
    ("C", "F", 2),
    ("D", "G", 3),
    ("E", "H", 4),
    ("F", "I", 5),
]

# 0, impossible to reach
print(num_ways_to_climb(tree, 6))

# 2
print(num_ways_to_climb(tree, 10))
