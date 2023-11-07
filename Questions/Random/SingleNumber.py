# 136. Single Number - Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

nums = [4,1,2,1,2]
def singleNumber(array):
    result = 0
    for num in array:
        result = result ^ num
        print(result)

print(singleNumber(nums))