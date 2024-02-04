class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)  #   ------> O(1)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, val):
        self.items.append(val)
        return "Element enqueued" # time complexity : O(n), spcae O(1)

    def dequeue(self):
        if self.isEmpty():
            print("List is Empty")
        else:
            return self.items.pop(0)  # time complexity : O(n), spcae O(1)

    def peek(self):
        if self.isEmpty():
            print("List is Empty")
        else:
            return self.items[0]

    def delete(self):
        self.items = None


queue = Queue()
print("Is Queue Emptry ?")
queue.isEmpty()
print("Enqueing Elements : \n")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue)
print("Dequeing Elements : \n")
queue.dequeue()
queue.dequeue()
print(queue)
print("Peek Elements")
print(queue.peek())

