class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepand(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def __str__(self):
        temp = self.head
        result = " "
        while temp:
            result += str(temp.value)
            if temp.next:
                result += " <-> "
            temp = temp.next
        return result

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def reverse_traverse(self):
        curr = self.tail
        while curr:
            print(curr.value)
            curr = curr.prev

    def search(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def get(self, index):
        if index < 0 and index >= self.length:
            return None
        if index < self.length // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.length - 1, index, -1):
                curr = curr.prev
        return curr

    def set(self, index, value):
        node = self.get(index)
        while node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        new_node = Node(value)
        if index == 0:
            self.prepand(value)
            return
        elif index == self.length:
            self.append(value)
            return
        else:
            temp = self.get(index - 1)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
        self.length += 1

    def pop(self):
        if not self.head:
            return print("None")
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return print("None here")
        curr = self.head.next
        curr.prev = None
        self.head.next = None
        self.head = curr
        self.length -= 1

    def pop_last(self):
        if self.head == None:
            return print("None")
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return print("None here")
        curr = self.tail.prev
        curr.next = None
        self.tail.prev = None
        self.tail = curr
        self.length -= 1

    def pop_any(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop()
        if index == -1:
            return self.pop_last()
        else:
            popped_element = self.get(index)
            popped_element.prev.next = popped_element.next
            popped_element.next.prev = popped_element.prev
            popped_element.prev = None
            popped_element.next = None
        self.length -= 1
        return popped_element


node = DoublyLinkedList()
node.append(10)
node.append(20)
node.append(30)
node.append(40)
node.prepand(100)
node.prepand(200)
node.prepand(300)
print(node)
print("Traversing the Nodes")
# node.traverse()
print("Traversing the Nodes in reverse")
# node.reverse_traverse()
print("Search method here")
# print(node.search(20))
print("Get method here")
# print(node.get(3))
print("Setting New Methods")
# node.set(4, 987)
print(node)
print("Inserting value at any position")
# node.insert(4, 899)
print(node)
print("Popping element")
# node.pop()
# node.pop_last()
node.pop_any(90)
print(node)
