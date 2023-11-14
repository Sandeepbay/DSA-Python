# Using Divide and Conquer Algorithm , We are finding the Fibanocci number of the required placeholder.

def fibanocci(n):
    if n < 1:
        return "Error message"
    if n == 1 :
        return 0
    if n == 2:
        return 1
    else:
        return fibanocci(n-1) + fibanocci(n-2)

print(fibanocci(7))