# Performing a binary Search

nums = [1,3,5,6]

def binarySearch(nums , target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target :
            return middle
        elif target < nums[middle]:
            end = middle - 1
        elif target > nums[middle]:
            start = middle + 1
    return start

print(binarySearch(nums , 7))

