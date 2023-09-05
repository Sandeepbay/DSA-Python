#Conditional Filter - Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def filter_dict(my_dict):
    return {k:v for k,v in my_dict.items() if v % 2 == 0 }
print(filter_dict(my_dict))
