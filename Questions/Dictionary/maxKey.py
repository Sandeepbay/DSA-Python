#Key with the Highest Value - Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

my_dict = {'a': 5, 'b': 9, 'c': 2}

def max_value_key(my_dict):
    return max(my_dict , key=my_dict.get)
print(max_value_key(my_dict))