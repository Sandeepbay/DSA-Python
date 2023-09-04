#Pairs - Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

pair_sum = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]

def pairs(arr , sum):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]+arr[j] == sum:
                print(arr[i],arr[j])
print(pairs(pair_sum , 7))