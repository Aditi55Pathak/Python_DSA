class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CDlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def cdll(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.prev = new_node
        new_node.next = new_node
        return self  # Return the CDlinkedList instance

    def insertion(self, value, location):
        if self.head is None:
            return "CDl is empty"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.prev = self.tail
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node

            elif location == -1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                curr = self.head
                index = 0
                while index < location - 1:
                    curr = curr.next
                    index += 1
                new_node.next = curr.next
                new_node.prev = curr
                curr.next.prev = new_node
                curr.next = new_node
            return "Linked List Sucessfully Created"

    def traverse(self):
        if self.head == None:
            return "LL empty"
        else:
            curr = self.head
            while curr:
                print(curr.value)
                if curr == self.tail:
                    break
                curr = curr.next
            return curr

    def reverse(self):
        if self.head == None:
            return "LL empty"
        else:
            curr = self.tail
            while curr:
                print(curr.value)
                if curr == self.head:
                    break
                curr = curr.prev
            return curr

    def search(self, target):
        if self.head == None:
            return "LL empty"
        else:
            curr = self.head
            while curr:
                if curr.value == target:
                    print("Element Found")
                    return
                curr = curr.next
                if curr == self.head:
                    break
            print("Element Not Found")

    def delete(self, loc):
        if self.head == None:
            return "LL empty"
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head.prev = self.head.next = None
                    self.head = self.head = None
                else:
                    curr = self.head.next
                    self.head.next = None
                    self.head.prev = None
                    curr.prev = self.tail.prev
                    self.head = curr
            elif loc == -1:
                if self.head == self.tail:
                    self.head.prev = self.head.next = None
                    self.head = self.head = None
                else:
                    curr = self.tail.prev
                    curr.next = self.head
                    self.head.prev = curr
                    self.tail.prev = self.tail.next = None
                    self.tail = curr
            else:
                curr = self.head
                index = 0
                while index < loc:
                    curr = curr.next
                    index += 1
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr.next = curr.prev = None
            return "Element deleted Sucessfully"

    def delete_all(self):
        if self.head == None:
            return "LL empty"
        else:
            self.tail.next = None
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
            print("Linked List deleted Sucessfully")


cdl = CDlinkedList()
print(cdl.cdll(5))
cdl.insertion(0, 0)
cdl.insertion(1, 1)
cdl.insertion(2, 2)
cdl.insertion(3, 3)
cdl.insertion(4, 4)
# Iterate and print values
print([node.value for node in cdl])
print("Traversing the Linked List")
cdl.traverse()
print("Traversing the Linked List in Reverse")
cdl.reverse()
print("Searching For element")
cdl.search(4)
print("Deletion")
cdl.delete(2)
print([node.value for node in cdl])
print("Deleting entire LinkedList")
cdl.delete_all()
