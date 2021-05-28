# Method: Dynamic Programming (Recursion with memoization)
def max_square(grid):
    r = len(grid)
    c = len(grid[0])
    dp = [[None] * c for _ in range(r)]

    def update(i, j):
        if dp[i][j] is not None:
            return dp[i][j]
        if i == 0 or j == 0:
            dp[i][j] = 1
        elif (
            len(set([grid[i][j], grid[i - 1][j], grid[i][j - 1], grid[i - 1][j - 1]]))
            == 1
        ):
            dp[i][j] = min(update(i - 1, j), update(i, j - 1), update(i - 1, j - 1)) + 1
        else:
            dp[i][j] = 1
        return dp[i][j]

    ans = 1
    for m in range(r):
        for n in range(c):
            ans = max(ans, update(m, n))
    return ans ** 2


sample1 = [[2, 2, 2, 8], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
# 16
print(max_square(sample1))

sample2 = [
    [1, 1, 2, 3, 5],
    [2, 3, 3, 4, 1],
    [1, 3, 3, 6, 1],
    [4, 4, 4, 4, 5],
    [4, 4, 4, 1, 2],
    [4, 4, 4, 6, 6],
]
# 9
print(max_square(sample2))

sample3 = [
    [1, 1, 3],
    [2, 2, 3],
    [2, 4, 3],
]
# 1
print(max_square(sample3))
