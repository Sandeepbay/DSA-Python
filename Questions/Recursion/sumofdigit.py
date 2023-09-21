# Find the sum of digit of a positive integer using  recursion.
# i.e input 45 = 4+5 = 9

def sumDigit(n):
    assert n >= 0 and int(n) == n , "Value of n should be positive integer"
    if n == 0:
        return 0
    else:
        return n%10  + sumDigit(int(n/10))
print(sumDigit(143))