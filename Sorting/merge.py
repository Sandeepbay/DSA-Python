# Merge Sort is a divide and conquer Algorithm
# Divide the input array in two halves and we keep halving recursively until they become too small that cannot be broken further.
# Merge halves by sorting them

customList = [2,5,1,9,3,7,4]

def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i = i + 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list[k] =  right_half[j]
            j += 1
            k += 1

    return list


print(mergeSort(customList))