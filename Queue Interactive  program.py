class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
q = Queue()
while True:
    print('Press 1 for insert')
    print('Press 2 for delete')
    print('Press 3 for quit')
    operation = int(input('What would you like to do ?? '))
    if operation == 1:
        n=int(input("enter a number to insert : "))
        q.enqueue(n)
    elif operation == 2:
        if q.isEmpty():
            print('Queue is empty.')
        else: print('Deleted value: ', q.dequeue())
    elif operation == 3:
        print("Dhanyawaad !!!! Dobara Zaroor Aayein")
        break
