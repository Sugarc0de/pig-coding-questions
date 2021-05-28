# Method: Dynamic Programming (Recursion with memoization)
def rotate_cooking(day: int, d_max: int, t_max: int) -> int:
    # dp stores number of ways where d_max and t_max
    dp = {}
    dp[(1, 0, 0)] = 1

    def recurse(day, d_max, t_max):
        if (day, d_max, t_max) in dp:
            return dp[(day, d_max, t_max)]
        if day == 1:
            ans = 1
            if d_max:
                ans += 1
            if t_max:
                ans += 1
            dp[(day, d_max, t_max)] = ans
            return dp[(day, d_max, t_max)]
        ans = 0
        if d_max > 0:
            ans += recurse(day - 1, d_max - 1, t_max)
        if t_max > 0:
            ans += recurse(day - 1, d_max, t_max - 1)
        ans += recurse(day - 1, d_max, t_max)
        dp[(day, d_max, t_max)] = ans
        return dp[(day, d_max, t_max)]

    recurse(day, d_max, t_max)
    return dp[(day, d_max, t_max)]


# Example: 2 days, dog cooks no more than 1 day, takeout no more than 1 day
# there are 7 unique ways in total.
# [(pig, pig), (pig, dog), (dog, pig), (pig, takeout), (takeout, pig),
# (takeout, dog), (dog, takeout)]
print(rotate_cooking(2, 1, 1))
