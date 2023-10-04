# 2455. Average Value of Even Numbers That Are Divisible by Three

#Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.
#Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

nums = [1,2,4,7,10]

def averageValue(nums):
    sum = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            if nums[i] % 3 == 0:
                sum = sum + nums[i]
                count = count + 1
    if count != 0:
        return int(sum/count)
    else:
        return 0



print(averageValue(nums))
 