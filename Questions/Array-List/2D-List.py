#2D Lists - Given 2D list calculate the sum of diagonal elements.
matrix = [[1,2,3],[4,5,6],[7,8,9]] 

def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum = sum + matrix[i][j]
    return sum

print(diagonal_sum(matrix))

