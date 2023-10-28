# 1. Two Sum - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

nums = [3,2,4]
target = 6

def twoSum(array , value):
    for i in range(len(array)):
        for j in range(i+1 , len(array)):
            new_array= []
            if array[i] + array[j] == value:
                new_array.append(i)
                new_array.append(j)
                return new_array
 
print(twoSum(nums , target))