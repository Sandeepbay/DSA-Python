#Creating a Stack Class
class Stack:
    def __init__(self , maxSize):
        self.maxSize = maxSize
        self.list = []

    #A Method to display the Stack
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    #A method to check if the stack is empty or not
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #A method to check if the stack is full or not    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    #A Method to add elements inside the stack      
    def push(self,value):
        self.list.append(value)

    #A method to remove element from the stack
    def pop(self):
        return self.list.pop()
    
    #A method to check the first element in the stack i.e last element pushed inside the stack
    def peek(self):
        return self.list[len(self.list) - 1]

    #A methos to delete entire stack
    def deleteStack(self):
        self.list = None
    
#Operations carried out 
new_Stack = Stack(5)
# print(new_Stack.isEmpty())
# print(new_Stack.isFull())
new_Stack.push(1)
new_Stack.push(2)
new_Stack.push(3)
new_Stack.push(4)
new_Stack.push(5)
# print(new_Stack.peek())
# new_Stack.deleteStack()
# print(new_Stack.pop())
print('\n')
print(new_Stack)

