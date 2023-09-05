#Common Elements - Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

list = []

def common_elements(tuple1, tuple2):
    for i in range(len(tuple1)):
        for j in range(len(tuple2)):
            if tuple1[i] == tuple2[j]:
                list.append(tuple1[i])
common_elements(tuple1, tuple2)
print(tuple(list))
            