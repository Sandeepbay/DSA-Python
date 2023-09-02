#Creating Array using Array module
import array

my_array = array.array('i')
#Printing my empty array
#print(my_array)
my_array_values = array.array('i' , [1,2,3,4,5])
#Printing my array which has values
#print(my_array_values)

#Creating Array using numpy module
import numpy as np

my_array = np.array([] , dtype='int')
#Printing an Empty Array
#print(my_array)

my_array_list = np.array([1,2,3,4])
#Printing my array which has values
#print(my_array_list)

#Inserting Element in the array
insert_array = array.array('i' , [1,2,3,4,5,6])
insert_array.insert(6,7)
#print(insert_array)

#Tranversing an Array
# arr1 = array.array('i' , [1,2,3,4,5])
# def tranverse(array):
#     for i in array:
#         print(i)

# tranverse(arr1)

#Acessing an element in the array

# arr1 = array.array('i' , [1,2,3,4,5,6,7,8])
# def accessElement(array , index):
#     if index >= len(array):
#         print("There is no element in this index")
#     else:
#         print(array[index])

# accessElement(arr1 , 4)

#Searching an element in the array using Linear Search

# arr1 = array.array('i' , [1,2,3,4,5])
# def search(array , target):
#     for i in range(len(array)):
#         if array[i] == target:
#             return i
#     return -1

# print(search(arr1 , 3))

#Deleting an element from the array

array = array.array('i' , [1,2,3,4,5,6])

array.remove(5)

#print(array)