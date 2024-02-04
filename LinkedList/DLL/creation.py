class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.prev} <- {self.value} -> {self.next} "


node = Node(10)
print(node)
