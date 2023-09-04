#Check if two Lists are in permutation or not. - Two Lists are in permutation if they have same element irrespective of the order.

list1 = [1,2,3,4]
list2 = [2,3,1,4]

def permuation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2 :
        return True
    else:
        return False
print(permuation(list1 , list2))