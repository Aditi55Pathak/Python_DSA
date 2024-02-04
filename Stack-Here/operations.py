class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def push(self, values):
        # Adds value to the top of the stack
        self.list.append(values)

    def pop(self):
        if self.list is None:
            return
        else:
            return self.list.pop()

    def peek(self):
        if self.list is None:
            return
        else:
           return self.list[len(self.list)-1]
        
    def delete(self):
        self.list=None



stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print(stack.isEmpty())
# stack.pop()
# stack.pop()
print("Stack after modification: ")
stack.peek()
print(stack)
stack.delete()
print("After deleting all elements from the stack")
