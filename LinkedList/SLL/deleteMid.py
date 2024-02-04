# Inserting element at any index


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

    def insertAny(self, index, value):
        newNode = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.head is None:
            self.head = self.tail = newNode
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            newNode.next = temp_node.next
            temp_node.next = newNode
        self.length += 1
        return True

    def __str__(self):
        temp_node = self.head
        result = " "
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    def traverse(self):  # Time complexity O(n)
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, index):
        current = self.head
        if index == -1:
            return self.tail
        elif index < -1 and index >= self.length:
            print("Invalid Index")
        for _ in range(index):
            current = current.next
        return current

    # Time complexity O(n)

    def set(self, index, value):
        temp_var = self.get(index)
        if temp_var:
            temp_var.value = value
            return True
        return False

    # Time complexity O(n)

    def pop_element(self):
        if self.length == 0:
            return None
        popped_element = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            popped_element.next = None
        self.length -= 1
        return popped_element

    # Time complexity O(n)

    def pop_element_end(self):
        if self.length == 0:
            return None
        popped_element = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_element

    def pop_element_any(self, index):
        if index < -1 and index >= self.length:
            return None
        if index == 0:
            return self.pop_element()
        elif index == self.length - 1 or index == -1:
            return self.pop_element_end()
        prev_node = self.get(index - 1)
        popped_element = prev_node.next
        prev_node.next = popped_element.next
        popped_element.next = None
        self.length -= 1
        return popped_element
 # Time complexity O(n)

sll = singleLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

print(sll)
print("After popping value")
a = sll.pop_element_any(3)
print(a)
