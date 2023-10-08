# Create buckets and distribute elements of array into buckets
# Sort buckets individually
# Merge buckets after sorting 

import math

customList = [8,1,3,5,2,4,7,6]

def insertionSort(customList):
    for i in range(1 , len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList

def bucketSort(list):
    numberOfBuckets = round(math.sqrt(len(list)))
    maxValue = max(list)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])
    for j in list:
        bucket = math.ceil(j * numberOfBuckets / maxValue)
        arr[bucket-1].append(j)
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            list[k] = arr[i][j]
            k+=1
    return list

print(bucketSort(customList))
