#Best Score - Given a list, write a function to get first, second best scores from the list.
#List may contain duplicates.

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0,90]

def first_second(my_list):
    my_list.sort(reverse=True)
    if myList[0] == myList[1]:
        return myList[0] ,  myList[2]
    else:
        return myList[0] ,  myList[1]
print(first_second(myList))