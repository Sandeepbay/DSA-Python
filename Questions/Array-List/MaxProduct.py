#Max Product of Two Integers - Find the maximum product of two integers in an array where all elements are positive.

list = [1,4,2,5,3]

def reverseProduct(arr):
    arr.sort(reverse = True)
    print(arr[0] * arr[1])
reverseProduct(list)