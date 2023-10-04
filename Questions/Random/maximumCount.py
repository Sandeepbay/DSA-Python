# 2529. Maximum Count of Positive Integer and Negative Integer.

#Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
#In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
#Note that 0 is neither positive nor negative.

customArray = [-3,-2,-1 , 0 , 1 ,2]

def maximumCount(array):
    pos = 0
    neg = 0
    for i in range(len(array)):
        if array[i] == 0:
            continue
        elif array[i] > 0:
            pos += 1
        else:
            neg += 1
    return max(pos , neg)
        


print(maximumCount(customArray))