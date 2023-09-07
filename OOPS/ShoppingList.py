class ShoppingList:
    def __init__(self,value,value1) -> None:
        self.value = value
        self.value1 = value1

list1 = ShoppingList("Milk" , "Curd")
list2 = ShoppingList("Eggs" , "Apple")
print(list1.value , list1.value1)
print(list2.value , list2.value1)