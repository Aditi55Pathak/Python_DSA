class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currnode = self.head
        while currnode:
            yield currnode
            currnode = currnode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        return False

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            poppedNode = self.LinkedList.head
            self.LinkedList.head = self.LinkedList.head.next
            return poppedNode.value

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            poppedNode = self.LinkedList.head  # Returns first element of stack
            return poppedNode.value

    def delete(self):
        self.LinkedList.head = None


customClass = Stack()
customClass.push(3)
customClass.push(2)
customClass.push(1)
print(customClass)
print("-------------------")
customClass.pop()
print(customClass)
print(customClass.isEmpty())
