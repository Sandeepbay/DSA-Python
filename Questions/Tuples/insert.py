#Insert at the Beginning - Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

input_tuple = (2, 3, 4)
value_to_insert = 1

my_list = []

def insert_value_front(input_tuple, value_to_insert):
    my_list.append(value_to_insert)
    for i in range(len(input_tuple)):
        my_list.append(input_tuple[i])
    return tuple(my_list)
print(insert_value_front(input_tuple, value_to_insert))
