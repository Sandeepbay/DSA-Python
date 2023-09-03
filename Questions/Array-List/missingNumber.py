#Missing Number - Write a function to find the missing number in a given integer array of 1 to 100.

import array

arr = array.array('i' , [1,2,3,4,5,6,7,9,10])

def missing_number(arr, n):
    sum1 = (n*(n+1))/2
    sum2 = sum(arr)
    num = sum1 - sum2 
    print(num)
missing_number(arr , 10)