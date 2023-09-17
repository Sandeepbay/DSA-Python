from collections import deque

customQueue = deque(maxlen=5)
customQueue.append(1)
customQueue.append(5)
customQueue.append(8)
customQueue.append(9)
customQueue.append(13)
print(customQueue)
#customQueue.popleft()
customQueue.clear()
print(customQueue)