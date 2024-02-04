class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currnode = self.head
        while currnode:
            yield currnode
            currnode = currnode.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        value = [str(x) for x in self.linkedlist]
        return " ".join(value)

    def enqueue(self, value):
        newnode = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = newnode
            self.linkedlist.tail = newnode
        else:
            self.linkedlist.tail.next = newnode
            self.linkedlist.tail = newnode

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            removedNode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return removedNode

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            return self.linkedlist.head

    def delete(self):
        self.linkedlist.head = self.linkedlist.tail = None


customeQueue = Queue()
customeQueue.enqueue(1)
customeQueue.enqueue(2)
customeQueue.enqueue(3)
print(customeQueue)
customeQueue.dequeue()
print(customeQueue)
print(customeQueue.peek())
customeQueue.delete()
print("Deleted Sucessfully")
