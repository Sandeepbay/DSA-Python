# 69. Sqrt(x) - Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

x = 8

def squareRoot(x):
    if x == 0:
        return 0
    low = 1
    high = x
    # global ans
    while low <= high:
        middle = (low + high) // 2
        if middle * middle <= x:
            low = middle + 1
            ans = middle
        else:
            high = middle -1
    return ans

print(squareRoot(x))