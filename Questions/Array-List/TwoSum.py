#leetcode #1 Question

list = [2,7,11,15]

def TwoSum(list , target):
    for i in range(len(list)):
        for j in range(i+1 , len(list)):
            if list[i] + list[j] == target:
                print(i,j)
TwoSum(list , 9)