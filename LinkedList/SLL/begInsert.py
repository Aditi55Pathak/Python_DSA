# Insertion in beginning

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


sll = singleLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
# print(sll.head.value)
# print(sll.tail.value)
print(sll)
# Time and Space Complexity O(1)
sll.prepend(60)
sll.prepend(70)
sll.prepend(80)
sll.prepend(90)
sll.prepend(100)

print(sll)
