#Creating  a Queue Class
class Queue:
    def __init__(self):
        self.queue = []

    #Creating a method to display the Queue
    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)
    
    #A method to check is the queue is empty or not
    def isEmpty(self):
        if self.queue == []:
            return True
        else:
            return False

    #A method to add Elements in the Queue
    def enqueue(self,value):
        self.queue.append(value)

    #A method to remove the first element of the Queue
    def dequeue(self):
        return self.queue.pop(0)
    
    #A method to know the first element in the Queue
    def peek(self):
        return self.queue[0]
    
    #A method to delete the entire Queue
    def deleteQueue(self):
        self.queue = []

#All operations carried out
new_Queue = Queue()
#print(new_Queue.isEmpty())
new_Queue.enqueue(1)
new_Queue.enqueue(2)
new_Queue.enqueue(3)
new_Queue.enqueue(4)
new_Queue.enqueue(5)
#print(new_Queue.dequeue())
#print(new_Queue.peek())
#new_Queue.deleteQueue()
print(new_Queue)
