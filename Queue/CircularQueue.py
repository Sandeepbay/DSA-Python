#Creating a class
class Queue:
    def __init__(self , maxSize):
        self.queue = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    #A method to display the Queue
    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)
    
    #A method to check if the Queue is Full or not
    def isFull(self):
        if self.start == 0 and self.top + 1 == self.maxSize:
            return True
        elif self.top + 1 == self.start:
            return True
        else:
            return False

    #A method to check if the Queue is Empty or not    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    #A method to add elements inside the Queue
    def enqueue(self,value):
        if self.isFull():
            return "The List is full , cannot add more elements"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                self.start = 0
            self.queue[self.top] = value

    #A method to remove elements from the Queue
    def dequeue(self):
        value = self.queue[self.start]
        self.queue[self.start] = None
        self.start += 1
        return value
    
    #A method to return the first element in the Queue
    def peek(self):
        if self.isEmpty():
            return "There are no elements in this list"
        else:
            return self.queue[self.start]

    #A method to delete an entire Queue    
    def deleteQueue(self):
        self.queue = self.maxSize * [None]
        self.start = self.top = -1
        
#Operations carried out        
new_Queue = Queue(5)
#print(new_Queue.isFull())
#print(new_Queue.isEmpty())
new_Queue.enqueue(1)
new_Queue.enqueue(4)
new_Queue.enqueue(7)
new_Queue.enqueue(9)
new_Queue.enqueue(13)
print(new_Queue)
#print(new_Queue.dequeue())
#print(new_Queue.peek())
new_Queue.deleteQueue()
print(new_Queue)