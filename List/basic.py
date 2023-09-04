#Creating Lists and Printing them

integer = [1,2,3,4]
#print(integer)
string = ["Milk" , "Curd" , "Eggs"]
#print(string)
mixedList = [0.2 , 1 , "LOL" , [3 , 0 , "Score"]]
#print(mixedList)

#Accessing Element
shoppingList = ["Milk" , "Curd" , "Eggs"]
#print(shoppingList[0])
#print(shoppingList[-2])

#Using in operator
#print("Eggs" in shoppingList)

#Traversing an array
# for i in range(len(shoppingList)):
#     shoppingList[i] = shoppingList[i] + "+"
#     print(shoppingList[i])

#Updating elements in the list
integers = [1,2,3,4,5]
integers[1] = 22
#print(integers)

#Inserting Elements in the list
#We can insert elements in 3 ways - insert() - We can insert element anywhere in the list , append() - we can insert element at the end of the array, extend() - we can insert another list to the current list using the extend function

list = [1,3,4,5,6]
list.insert(1,2)
#print(list)
list.append(7)
#print(list)
list_d = [8,9,10]
list.extend(list_d)
#print(list)

#Slicing elements and updating them
#print(list[0:3])

#Deleting elements from the list - we can do delete elements using 3 methods - delete() - we can delete by using the index , it doesnt return the deleted value , pop()  - we can delete by using the index here - we can either remove the last element or any other element by giving the parameter, remove() - we can remove element by just providing the value

lists = [1,3,4,5,6]
#lists.remove(1)
#print(lists)
#print(lists.pop(3))
#print(lists)

#Searching an element in the list
#Using the in operator

my_list = [10 , 30 , 40 , 50 , 60 , 70]
target = 50

# if target in my_list:
#     print(f"{target} has been found")
# else:
#     print(f"{target} has not been found")

#Using Linear search 

def linear_serach(array , key):
    for i , value in enumerate(array):
        if value == key:
            return i
    return -1 

#print(linear_serach(my_list , target))

#The List operations are (+) - It adds up two lists , (*) - This operation repeats the list as many number of times we want.

a = [0,1]
a = a * 3
#print(a) 

#List functions - The different type of functions are - 1. sum() 2. len() 3. max() 4. min()

#Challenge - 

# list = []
# while(True):
#     inp = input("Enter a number ")
#     if(inp == "done"):
#         break
#     list.append(int(inp))
# average = sum(list)/len(list)
#print(average)

#To convert a string to a list , we are gonna use list()
#To convert a list to a string , we are gonna use join()
#To split a string , we are gonna use split()

#List Comprehension
# new_list = [new_item for item in prev_list if condition] u can also else statment and can move the if operation before 'for'

prev_list = [1,2,3]
new_list = [i*3 for i in prev_list]
#print(prev_list)
#print(new_list)



