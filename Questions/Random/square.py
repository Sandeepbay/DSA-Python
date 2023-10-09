# 977. Squares of a Sorted Array
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

nums = [-4,-1,0,3,10]
new_list = []

def sortedSquares(list):
    for i in list:
        new_list.append(i*i)

    for i in range(len(new_list)- 1):
        for j in range(len(new_list) - i - 1):
            if new_list[j] > new_list [j+1]:
                new_list[j] , new_list[j+1] = new_list[j+1], new_list[j]
                
    return new_list
    
    
print(sortedSquares(nums))