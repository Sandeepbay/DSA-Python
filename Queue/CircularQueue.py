#Creating a class function
class Queue:
    def __init__(self , maxSize):
        self.maxSize = maxSize
        self.queue = maxSize * [None]
        self.start = -1
        self.top = -1

    #A method to display the Queue
    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)
    
    #A method to check if a queue is full or not
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1  == self.maxSize:
            return True
        else:
            return False

    #A method to check if the queue is empty or not    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def enqueue(self,value):
        self.queue.append(value)

#Operations carried out        
new_Queue = Queue(5)
#print(new_Queue.isFull())
#print(new_Queue.isEmpty())
new_Queue.enqueue(1)
print(new_Queue)    

