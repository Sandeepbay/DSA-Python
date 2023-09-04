#Common Keys - Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    #print(result)
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
print(merge_dicts(dict1, dict2))
