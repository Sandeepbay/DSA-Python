# Hashing - Hashing is a method of sorting and indexing data. The idea behind is to allow large amounts of data to be indexed using keys commonly created by formulas.
# So what happens here is , the strings that have to be indexed is passed through some function while will generate its equivalent number. This number is the index for the following string. We can access the string using this number as this number is constant for the following string.

#It is efficent for Search operation.

# Hashing Terminology

# Hash Function - It is a function that can be used to map of arbitary size to data of fixed size.
# Key - Input data by a user.
# Hash Value - A value that is returned by Hash function
# Hash Table - It is a data structure which implements an associative array abstract data type , a structure that can map keys to values.
# Collision - A collision occurs when two different keys to a hash function produce the sae output.

def mod(number, cellNumber):
    return number % cellNumber


print(mod(400, 24))


def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

print(modASCII("ABC", 24))