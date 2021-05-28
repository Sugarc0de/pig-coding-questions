# Method 1: Sliding Window
def meet_idols_1(idols):
    sorted_idols = list(sorted(idols))
    idols = sorted_idols + [24 + i for i in sorted_idols]
    l, r, max_count, count = 0, 0, 0, 0
    while idols[r] - idols[l] <= 12:
        r += 1
        count += 1
    max_count = count
    while r < len(idols):
        lmin = idols[r] - 12
        while idols[l] <= lmin:
            l += 1
            count -= 1
        count += 1
        r += 1
        max_count = max(max_count, count)
    return max_count


# Method 2: Binary Search
def meet_idols_2(idols):
    sorted_idols = list(sorted(idols))
    idols = sorted_idols + [24 + i for i in sorted_idols]

    ans = 0
    for ix in range(len(idols)):
        # [ix, lo] is the idols that dog meets
        lo = ix
        hi = len(idols)
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if idols[mid] <= 12 + idols[ix]:
                lo = mid
            else:
                hi = mid
        ans = max(ans, lo - ix + 1)
    return ans


############# Method 1 ################

# 4
print(meet_idols_1([1, 2, 3, 4]))

# 2
print(meet_idols_1([0, 12]))

# 3
print(meet_idols_1([17, 4.9, 5, 5.1]))

# 13
print(meet_idols_1(list(range(0, 24))))

############# Method 2 ################

# 4
print(meet_idols_2([1, 2, 3, 4]))

# 2
print(meet_idols_2([0, 12]))

# 3
print(meet_idols_2([17, 4.9, 5, 5.1]))

# 13
print(meet_idols_2(list(range(0, 24))))
