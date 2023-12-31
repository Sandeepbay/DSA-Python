# A Method to implement Binary Search
customArray = [2,6,12,23,35,45]

def binarySearch(array , value):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end)//2
        if array[middle] == value:
            return array[middle]
        elif value <= array[middle]:
            end = middle - 1
        elif value >= array[middle]:
            start = middle + 1
    return "Element has not been Found"

print(binarySearch(customArray , 2))
print(binarySearch(customArray , 6))
print(binarySearch(customArray , 23))
print(binarySearch(customArray , 12))
print(binarySearch(customArray , 35))
print(binarySearch(customArray , 45))
print(binarySearch(customArray , 60))