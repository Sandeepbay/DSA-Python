# A real time project where the user enters how many number of days we are gonna provide temperature.
#After that the user , provide the temperture for each day.
#The program should return the average temperature of all such days.
#Additionaly , it should also return the number of days the temperature is above the avergae temperature.

import array

temp_array = array.array('i' , [])
nod = int(input("Enter Number of days "))
for i in range(nod):
    day = int(input(f"Enter {i+1} day's temperature "))
    temp_array.append(day)
average = round(sum(temp_array)/len(temp_array),2)
print(f"Average Temperature is {average}")

#Traversing through the arrayto check if the days temperature is greater than average temperature

count = 0
for i in range(len(temp_array)):
    if temp_array[i] > average:
        count = count + 1
print(f"{count} number of days is greater than the average")
        
