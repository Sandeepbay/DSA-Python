# In bubble Sort , we repeatedly compare each pair of adjacent items and swap them if they are in the wrong order

def bubbleSort(customList):
    for i in range(len(customList)- 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList [j+1]:
                customList[j] , customList[j+1] = customList[j+1], customList[j]
    print(customList)

list = [3,2,5,4,1]
print(bubbleSort(list)) 