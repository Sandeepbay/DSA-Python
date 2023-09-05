#Sum and Product - Write a function that calculates the sum and product of all elements in a tuple of numbers.

input_tuple = (1, 2, 3, 4)

def sum_product(input_tuple):
    sum = 0
    product = 1
    for i in range(len(input_tuple)):
        sum = sum + input_tuple[i]
        product = product * input_tuple[i]        
        print(product)
    return (sum,product)
print(sum_product(input_tuple))

