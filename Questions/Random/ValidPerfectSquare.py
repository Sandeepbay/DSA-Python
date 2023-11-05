# 367. Valid Perfect Square - Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

num = 169

def validPerfectSquare(num):
    low = 1
    high = num
    while low <= high:
        middle = (low + high) // 2
        if middle * middle == num:
            return True
        elif middle * middle < num:
            low = middle + 1
        else:
            high = middle -1
    return False

print(validPerfectSquare(num))