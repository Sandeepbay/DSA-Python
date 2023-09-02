from array import * 

#1. Create an array and traverse

array1 = array('i' , [1,2,3,4,5])
print("Step 1")
for i in array1:
    print(i)

#2. Access individual elements through indexes

print("Step 2")
print(array1[0])

#3. Append any value to the array using append() method
#append() - This function is used to insert elements in the end of the array
print("Step 3")
array1.append(6)
print(array1)

#4 . Insert value in an array using insert() method

print("Step 4")
array1.insert(6,7)
print(array1)

#5. Extend Python array using extend() function
#extend() - Extends the existing array with another array.

print("Step 5")
array2 = array('i' , [10,11,12])
array1.extend(array2)
print(array1)

#6. Add Items from list into array using fromList() method
# fromList() - Add items to the array susing list

print("Step 6")
list = [15,16,17]
array1.fromlist(list)
print(array1)

#7. Remove any array element using remove() method

print("Step 7")
array1.remove(17)
print(array1)

#8. Remove last array element using pop() method

print("Step 8")
array1.pop()
print(array1)

#9. Fetch any element through its index using index() method
#index() - this function provides the index of any element

print("Step 9")
print(array1.index(15))

#10. Reverse a python array using reverse() method

print("Step 10")
array1.reverse()
print(array1)

#11. Get array buffer information through buffer_info() method
#buffer_info() - This method provides you the array buffer start address in the memory and the number of elements.

print("Step 11")
print(array1.buffer_info())

#12. Check for the number of occurences of an element using count()
print("Step 12")
print(array1.count(5))

#13. Convert array to list with same elements using toList()
print("Step 13")
print(array1.tolist())

#14. Slice Elements in the array

print("Step 14")
array1.reverse()
print(array1[:5])


 