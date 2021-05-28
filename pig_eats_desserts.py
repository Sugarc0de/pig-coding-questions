# Method: Binary Search
def eat_desserts(desserts, m):
    sorted_desserts = list(sorted(desserts))
    ways = 0
    for ix, cal in enumerate(sorted_desserts):
        lo = ix
        hi = len(sorted_desserts)
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if sorted_desserts[mid] + cal >= m:
                hi = mid
            else:
                lo = mid
        ways += len(desserts) - lo - 1
    return ways


# 19
print(eat_desserts([1, 1, 2, 4, 4, 4, 5, 7], 6))

# 0
print(eat_desserts([1, 4, 5, 3, 2, 1], 10))

# 6
print(eat_desserts([2, 2, 2, 2], 4))
