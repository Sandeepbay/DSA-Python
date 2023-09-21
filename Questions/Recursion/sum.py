# Find the sum of digits of a positive integer using  recursion.

def sum(n):
    assert n>= 0 and int(n) == n , "Value of n should be positve and integer"
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
print(sum(8))