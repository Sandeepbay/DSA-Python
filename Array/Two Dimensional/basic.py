import numpy as np

#Creating and Displaying a 2 Dimensional Array

#Monday - 10,13,23,21
#Tuesday - 11,27,32,9
#Wednesday - 25,23,12,15
#Thursday - 9,13,15,20

dArray = np.array([[10,13,23,21],[11,27,32,9],[25,23,12,15],[9,13,15,20]]) 
print(dArray)

#Adding row and column - 
# Using insert() method - 
#Adding row
TwoDArray = np.insert(dArray , 0 , [[1,2,3,4]] , axis = 0)
#print(TwoDArray)
#Adding column
TwoDArray = np.insert(dArray , 0 , [[1,2,3,4]] , axis = 1)
#print(TwoDArray)

# Using append() method - It adds row and column in the end (no need to give the index) 
#Adding row
TwoDArray = np.append(dArray ,[[1,2,3,4]] , axis = 0)
#print(TwoDArray)
#Adding column
TwoDArray = np.append(dArray ,[[1,2,3,4]] , axis = 0)
#print(TwoDArray)

#Accessing an element

# def accessElement(dArray , rowIndex , colIndex ):
#     if rowIndex >= len(dArray) or colIndex >= len(dArray[0]):
#         print("There is no element in this index")
#     else:
#         print(dArray[rowIndex][colIndex])

# accessElement(dArray , 1 , 2) 

#Traversing an array

# def traversing(dArray):
#     for i in range(len(dArray)):
#         for j in range(len(dArray)):
#             print(dArray[i][j])

# traversing(dArray)

#Searching an element in 2 Dimensional Array

# def search(dArray , target):
#     for i in range(len(dArray)):
#         for j in range(len(dArray[0])):
#             if dArray[i][j] == target:
#                 return "Found the element" + " " + str(i) + " " + str(j)
#     return "Didnt found the element"

# print(search(dArray , 12))

# Deleting a row or column
#Deleting the first row 
newTArray = np.delete(dArray , 0 , axis=0)
#print(newTArray)
#Deleting the first column 
newTArray = np.delete(dArray , 0 , axis=1)
#print(newTArray)