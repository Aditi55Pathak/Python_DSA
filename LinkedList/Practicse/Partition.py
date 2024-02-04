class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
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

    def partition(self, n):
        before_head = before_tail = Node(0)
        after_head = after_tail = Node(0)

        current_node = self.head

        while current_node:
            if current_node.value < n:
                before_tail.next = current_node
                before_tail = before_tail.next
            else:
                after_tail.next = current_node
                after_tail = after_tail.next

            current_node = current_node.next

        # Connect the two partitions
        before_tail.next = after_head.next
        after_tail.next = None

        # Update the head of the linked list
        self.head = before_head.next

    def __str__(self):
        temp_node = self.head
        result = " "
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result


# Example usage:
if __name__ == "__main__":
    ll = SingleLinkedList()
    values = [3, 5, 8, 5, 10, 2, 1]
    for value in values:
        ll.append(value)

    print("Original Linked List:")
    print(ll)

    n = 5
    ll.partition(n)

    print("\nLinked List after Partitioning around", n)
    print(ll)
