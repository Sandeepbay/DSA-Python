#Creating a Tuple

myTuple = ('a','b','c','d','e')
#myTuple1 = ('a',)
#myTuple2 = tuple()
myTuple3 = tuple('abcdef')
# print(myTuple)
# print(myTuple1)
# print(myTuple2)
# print(myTuple3)

#Accessing an element
#print(myTuple[2])

#We can also use slicing just like the lists.
#print(myTuple[2:5])

#Traversing inside a Tuple
# for i in range(len(myTuple)):
#     print(myTuple[i])

#Searching an element in a tuple

#print('a' in myTuple)
#print(myTuple.index('c'))
# def search(tuple , target):
#     for i in range(len(tuple)):
#         if tuple[i] == target:
#             return f"The {target} is found in index {i}"
#     return "Target has not been found"
# print(search(myTuple , 'd'))

#Tuple builtin functions and methods
# 1. (+) - It concatenates two tuples together.
# 2. (*) - It is used for repition. We can have a tuple as many types as we want using * operator.
# 3. (in) - it checks if an element is present in the tuple or not. Returns boolean value.
# 4. (count) - It returns the number of times a element is present in the tuple.count
#print(myTuple.count('a')) 
# 5. (index) - It returns the index of element present in the tuple.
# 6. (len) - It returns the length of the tuple.
# 7. (max) - It returns the maximum element inside the tuple
# 8. (min) -  It returns the minimum element inside the tuple
# 9. (tuple) - It converts the list into a tuple