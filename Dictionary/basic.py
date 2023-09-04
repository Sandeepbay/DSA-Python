#Creating a Dictionary

my_dict = {"one":"Eggs" , "two":"Milk" , "three":"Curd"}
#print(my_dict)

#Updating a Dictionary
dict = {"Name":"Sandeep" , "Age":20}
dict["Age"] = 21
#print(dict)

#Inserting new key value pair
dict["Address"] = "India"
#print(dict)

#Traversing in a dictionary
def traversing(dic):
    for key in dic:
        print(key , dic[key])
#traversing(dict)

#Searching for an element
def search(dic , value):
    for key in dic:
        if dic[key] == value:
            return key,value
    return "Value is not present"
# print(search(dict , "India"))

#Deleting a pair in dictionary
#There a four methods to delete a key value pair in a dictionary.
#1. pop() - This method will remove the pair and also return the value that is removed
# dict.pop("Name")
# print(dict)
#2. popitem() - This method will remove the last pair in the dictionary . It returns both the key and value pair.
# dict.popitem()
# print(dict)
#3. clear() - This method will remove all the pairs in the dictionary
# dict.clear()
# print(dict)
#4. del - This method will remove  the pair in the dictionary. Key should be provided
# del dict["Name"]
# print(dict)

#Dictionary Methods - 
#1. copy() - Makes a new dictionary wihout changing the previous one
#2. fromkeys() - The fromkeys method creates a new dictionary from given sequence of elements with value provided by user. 
new_dict = {}.fromkeys([1,2,3],0)
#print(new_dict)
#3. get() -  The get method returns the value for specified key if the key is in the dictionary.
#4. items() - The items method returns a view object that displays a list of dictionaries, key value tuple pairs.
#5. keys() - The keys method returns a view object that displays the list of all keys in the dictionary.
#6. setdefault() - The setdefault method returns the value of key if key is in the dictionary. If not, it inserts key with a value to the dictionary. 
#7. values() - The values method returns a view object that displays the list of all values in the dictionary.
#8. update() - The update method updates the dictionary with the elements from another dictionary object or from an iterable of key value pairs.

#Dictionary Operations/Builtin Methods
#1. in and not in operator -  To check if keys are present in the dictionary.
#2. all() - It checks the keys of the dictionary. If all the keys are True it returns true or else it returns False. (0 and False are false keys) - This works as AND Truth Table.
#3. sorted() - This functions sort the keys in the dictionary and returns the dictionary.
#4. any() -  It also checks the keys of the dictionary. If all the keys are True it returns true or else it returns False. (0 and False are false keys) - This works as OR Truth Table.