import queue as q

customQueue = q.Queue(maxsize=5)
print(customQueue.empty())
customQueue.put(1)
customQueue.put(3)
customQueue.put(5)
customQueue.put(7)
customQueue.put(9)
print(customQueue.full())
#Deleting element from thr Queue
print(customQueue.get())
print(customQueue.qsize())