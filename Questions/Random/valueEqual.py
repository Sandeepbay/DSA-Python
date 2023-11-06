# Geek for Geeks - Love Babbar DSA Sheet
# Value equal to index value
# Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).
# Note: There can be more than one element in the array which have the same value as its index. You need to include every such element's index. Follows 1-based indexing of the array.

arr = [15, 2, 45, 12, 7]

def valueEqualToIndex(arr, n):
    for i in range(n):
        if i == arr[i-1]:
            return i
    return False


print(valueEqualToIndex(arr,5))