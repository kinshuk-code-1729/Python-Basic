import queue
L = queue.Queue(maxsize=3)
# qsize() give the maxsize
# of the Queue
print(L.qsize())
L.put(5)
L.put(3)
L.put(1)
# Return Boolean for Full
# Queue
print("Full: ", L.full())
print(L.get())
print(L.get())
print(L.get())
print("Empty: ", L.empty())
