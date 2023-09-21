# Product of Array - Write a function called productOfArray which takes in an array of numbers and returns the product of them all.
import array

arr1 = array.array('i' , [1,2,3])
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * productOfArray(arr[1:])
print(productOfArray(arr1))