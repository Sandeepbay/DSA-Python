# 268. Missing Number - Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# This code works but there is a runtime error , so try to do the same with less runtime error. (Maybe without using for loop)

nums = [3,0,1]

def missingNumber(nums):
    # 1st Method
    # n = len(nums) + 1
    # for i in range(1,n):
    #     if i in nums:
    #         continue
    #     return i

    # 2nd Method - This method works in leetcode
    value = set(range(len(nums) + 1))
    for num in nums:
        value.remove(num)
    return value.pop()


print(missingNumber(nums))