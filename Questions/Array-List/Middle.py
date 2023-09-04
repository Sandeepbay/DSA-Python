#Middle Function - Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

list = [1,2,3,4,5,6]

def middle(list):
    my_list = list[1:len(list)-1]
    print(my_list)
middle(list)