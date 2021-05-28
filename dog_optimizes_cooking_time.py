# Method: Array
def optimize_cooking(t):
    sorted_t = list(reversed(sorted(t, key=lambda x: x[2])))
    # get the abs max end time for cooking
    abs_end = []
    last_end = 0  # abs time that last step ends
    for ig, pt, ct in sorted_t:
        # abs end time
        end = last_end + pt + ct
        last_end += pt
        abs_end.append(end)
    return max(abs_end)


# 16
print(
    optimize_cooking(
        [("meat", 4, 7), ("pepper", 5, 3), ("cabbage", 5, 2), ("green onions", 1, 1)]
    )
)
