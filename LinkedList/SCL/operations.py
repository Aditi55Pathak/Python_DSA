class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = self.head  # Set next to the head for circularity
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepand(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length and index < 0:  # If index is out of bound
            raise Exception("Index Out Of Bound !")
        if index == 0:  # If index is at first position
            if self.length == 0:  # If head and tail are pointing towards NONE
                self.head = self.tail = new_node
            else:
                new_node.next = self.head  # If all clear, locate the first element
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:  # If index is at last position
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = (
                self.head
            )  # Usual implementaion for inserting element at any pos
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = " "
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " -> "
        return result

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def search(self, target):
        curr = self.head
        while curr is not None:
            if curr.value == target:
                return True
            curr = curr.next
            if curr == self.head:
                break
        return False

    def get(self, index):
        if index == -1:
            return self.tail
        elif index < 0 or index >= self.length:
            return None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        return curr

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop(self):
        poppped_node = self.head
        if self.length == 0:
            None
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            poppped_node.next = None
        self.length -= 1
        return poppped_node

    def pop_end(self):
        popped_element = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
        self.length -= 1
        return popped_element

    def pop_any(self, index):
        if index < 0 and index >= self.length:
            return None
        elif index == 0:
            return self.pop()
        elif index == -1:
            return self.pop_end()
        else:
            prev = self.get(index - 1)
            popped_element = prev.next
            prev.next = popped_element.next
            popped_element.next = None
        self.length -= 1
        return popped_element

    def delete_all(self):
        if self.length == 0:
            None
        self.tail.next = None
        self.head = self.tail = None
        self.length = 0


csl = CSLinkedList()
csl.prepand(100)
csl.prepand(200)
csl.append(10)
csl.append(20)
csl.append(30)
csl.append(40)
csl.append(50)
csl.append(60)
print("Before Inserting value")
print(csl)
print("After Inserting Value")
csl.insert(2, 900)
csl.insert(7, 800)
csl.insert(0, 1000)
print(csl)
print("Traversing the Linked List")
csl.traverse()
print("Searching elements through out the loop")
print(csl.search(20))
print(csl.search(89))
print("getting elements through out the loop with index")
print(csl.get(90))
print("Setting the value")
csl.set(2, 87)
print(csl)
print("Popping the the first Value")
csl.pop()
print(csl)
print("Popping at end of linked list")
csl.pop_end()
print(csl)
print("Popping element from sepecific location")
csl.pop_any(7)
print(csl)
print("Delete full linked list")
csl.delete_all()
print(csl, "Everything deleted")

# Space complexity of all operations is O(1)
