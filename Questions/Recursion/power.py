# Find the power of a number using recursion.

def power(base , expo):
    assert expo >= 0 and int(expo) == expo , "Value of exponent should be positive and integer"
    if expo == 0:
        return 1
    else:
        return base * power(base , expo-1)
print(power(2,-4))