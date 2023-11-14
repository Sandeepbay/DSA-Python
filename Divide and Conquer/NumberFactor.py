# Using Divide and Conquer algorithm , You have been given a number N  , find how many ways u can express N by using the sum of either 1,3 and 4.
# For Example - If N = 5 ,Then u should return 6 as the answer. {1,1,1,1,1}{1,4}{4,1}{1,1,3}{1,3,1}{3,1,1} 

def numberFactor(n):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        return subP1 + subP2 + subP3

print(numberFactor(6)) 