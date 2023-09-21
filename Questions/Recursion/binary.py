# Write a program to convert decimal to binary number using recursion.

def binary(n):
    assert int(n) == n , "Value of n should be integer"
    if n == 0:
        return 0
    else:
        return n%2 + 10 * binary(int(n/2))

print(binary(15))