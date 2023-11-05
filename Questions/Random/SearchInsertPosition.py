# 35. Search Insert Position - Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

nums = [1,3,5,6,8,9]
target = 7

def searchInsertPosition(num , target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = (start + end) // 2
        if target == nums[middle]:
            return middle
        elif target <= nums[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return start

print(searchInsertPosition(nums , target))