# 217. Contains Duplicate - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

nums = [1,2,3,5]

# 1st Method

# def containsDuplicate(array):
#     for i in range(len(array)):
#         print(i , "I")
#         for j in range(i+1 , len(array)):
#             print(j , "J")
#             if array[i] == array[j]:
#                 return True
#     return False

# 2nd Method

def containsDuplicate(array):
    seen = set()
    for i in array:
        if i in seen:
            return True
        seen.add(i)
    return False

print(containsDuplicate(nums))