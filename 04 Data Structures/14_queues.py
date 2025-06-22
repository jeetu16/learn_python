# Queue : Queue works on FIFO behavior(First In First Out)
from collections import deque
# when we use list as a queue and remove data from start as queue works it will be more unefficient. Because we have to move lots of items in memory if we use it for large amount of data. To solve efficiency problem we can use dequeue.

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()
print(queue)
