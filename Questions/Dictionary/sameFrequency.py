#Same Frequency - Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

def check_same_frequency(list1, list2):
    sorted(list1)
    sorted(list2)
    for i in list1:
        for j in list2:
            if i == j:
                return False
    return True
print(check_same_frequency(list1, list2))