# In quick sort , we take a pivot element as using this pivot element we sort the array.

customList = [2,5,1,9,3,7,4]

def quickSort(list):
    if len(list) <= 1:
        return list
    
    pivot = list[len(list) // 2]
    left = [x for x in list if pivot > x]
    middle = [x for x in list if pivot == x]
    right = [x for x in list if pivot < x]

    return quickSort(left) + middle + quickSort(right)


print(quickSort(customList))