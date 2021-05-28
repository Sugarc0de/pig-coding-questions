# Method: Dynamic Programming (Recursion with memoization)
def buy_pigcoin(rates, M, K):
    dp = {}
    rates = rates

    def get_max_cash_and_coin(ix, M, K):
        if ix in dp:
            return dp[ix]  # max cash, max pigcoin on that day
        if ix == 0:
            dp[ix] = (M, (M - K) / rates[ix])
        else:
            max_cash, max_coin = get_max_cash_and_coin(ix - 1, M, K)
            dp[ix] = (
                max(max_cash, (max_coin * rates[ix]) - K),
                max((max_cash - K) / rates[ix], max_coin),
            )
        return dp[ix]

    get_max_cash_and_coin(len(rates) - 1, M, K)
    return dp[len(rates) - 1][0]


# only one day, 2
print(buy_pigcoin([5], 2, 3))

# 2, can't buy anything
print(buy_pigcoin([1, 5], 2, 3))

# 47 after buying and selling
print(buy_pigcoin([1, 5], 13, 3))

# 47, same answer
print(buy_pigcoin([3, 2, 1, 5, 4], 13, 3))

# 80, double it 3 times
print(buy_pigcoin([2, 1, 2, 1, 2, 1, 2], 10, 0))
