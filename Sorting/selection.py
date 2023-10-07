# In selection Sort , we repeatedly find the minimum element and move it to the sorted part of the array to make the unsorted part sorted.

list = [3,2,5,4,1]
def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1 , len(customList)):
            if customList[j] < customList[min_index]:
                min_index = j
        customList[i] , customList[min_index] = customList[min_index] , customList[i]
    return customList
print(selectionSort(list))