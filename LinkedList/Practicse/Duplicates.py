class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class singleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = " "
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    def remove_duplicates(self):
        curr = self.head
        if curr is None:
            return
        nxt = curr.next

        while curr.next is not None:
            if nxt is not None and curr.value == nxt.value:
                curr.next = nxt.next
                nxt = nxt.next
            else:
                curr = curr.next
                if nxt is not None:
                    nxt = nxt.next

        return self.head


sll = singleLinkedList()
sll.append(1)
sll.append(2)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(4)
sll.append(4)
sll.append(5)
print(sll)
print("Removing Duplicates")
sll.remove_duplicates()
print(sll)
