class Node:
    def __init__(self, value):
        self.value = 10
        self.next = None


# Time complexity: O(1)
class singleLinkedList:
    def __init__(self, value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1


# Time complexity: O(1)

sl = singleLinkedList(10)
print(sl.head.value)

