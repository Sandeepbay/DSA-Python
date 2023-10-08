# In heap Sort , 1. Insert data into the heap Tree
# 2. Extract data into the heap Tree

customList = [2,5,1,9,3,7,4]

def heapify(list , n , i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[left] < list[smallest]:
        smallest = left

    if right < n and list[right] < list[smallest]:
        smallest = right

    if smallest != i:
        list[i] , list[smallest] = list[smallest] , list[i]
        heapify(list , n , smallest)

def heapSort(list):
    n = len(list)

    for i in range(n//2 -1, -1 , -1):
        heapify(list , n , i)

    for i in range(n-1 , 0 , -1):
        list[0] , list[i] = list[i] , list[0]
        heapify(list , i , 0) 
    list.reverse()

    return list

print(heapSort(customList))
