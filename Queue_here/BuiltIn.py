# Collection module

from collections import deque

customeQueue = deque(maxlen=3)
print(customeQueue)

customeQueue.append(1)
customeQueue.append(2)
customeQueue.append(3)
print(customeQueue)
customeQueue.popleft()
print(customeQueue)
customeQueue.clear()
print("All Clear")

# Queue module

# import queue as q

# cq = q.Queue(maxsize=3)
# print(cq.empty())
# cq.put(10)
# cq.put(20)
# cq.put(30)
# cq.put(40)
# print(cq.full())
# print(cq.get())
# print(cq.qsize())


