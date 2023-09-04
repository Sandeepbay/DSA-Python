#Duplicate Number - Write a function to remove the duplicate numbers on given integer array/list.

duplicates = [1, 1, 2, 2, 3, 4, 5]

def remove(duplicates):
    mylist = []
    for element in duplicates:
        if element not in mylist:
            mylist.append(element)
    return mylist
print(remove(duplicates))