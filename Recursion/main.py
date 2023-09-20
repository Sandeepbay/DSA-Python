# Performing the same operation multiple times with different inputs
# In every step we try smaller inputs to make the problem smaller
# Base condition is needed to stop the recursion , otherwise infinite loop will occur.

#Factorial Number:
def factorial(n):
    assert n>= 0 and int(n) == n , "Value of n should be positive integer"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))

# Fibonacci Series:
def fibonacci(n):
    assert n >= 0 and int(n) == n , "The value should be positive integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))