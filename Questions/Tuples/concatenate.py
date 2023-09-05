#Concatenate - Write a function that takes a tuple of strings and concatenates them, separating each string with a space.


input_tuple = ('Hello', 'World', 'from', 'Python')

def concatenate_strings(input_tuple):
    concatenated = ' '.join(input_tuple)
    return concatenated
print(concatenate_strings(input_tuple))