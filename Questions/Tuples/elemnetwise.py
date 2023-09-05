#Elementwise Sum - Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
my_list = []

def tuple_elementwise_sum(tuple1, tuple2):
    for i in range(len(tuple1)):
        for j in range(len(tuple2)):
            if i == j:
                my_list.append(tuple1[i] + tuple2[j])
tuple_elementwise_sum(tuple1,tuple2)
print(tuple(my_list))