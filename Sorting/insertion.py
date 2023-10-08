# In Insertion Sort, divide the given array into two parts. Take first element from unsorted array and find its correct position in sortd array. Repeat until sorted array is empty.

list = [4,5,2,1,3]
def insertionSort(customList):
    for i in range(1 , len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList
print(insertionSort(list))