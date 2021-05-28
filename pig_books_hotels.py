# Method: Binary Search
def book_hotels(hotels, D):
    sorted_hotels = sorted(hotels)
    ans = 0
    for ix, val in enumerate(sorted_hotels):
        lo = ix
        hi = len(hotels)
        while hi - lo > 1:
            mid = (hi + lo) // 2
            dist = hotels[mid] - val
            if dist <= D:
                lo = mid
            else:
                hi = mid
        ans += lo - ix
    return ans


# one value, 0
print(book_hotels([4], 5))

# negative values, 3
print(book_hotels([-1, -3, 0, 4, 5], 2))

# no value, 0
print(book_hotels([1, 4, 6, 9, 11], 1))

# dup values, 17
print(book_hotels([-2, -2, 0, 1, 3, 3, 6.5], 5))
