class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def Push(self, values):
        if self.isFull():
            print("Stack is Full!!")
        else:
            self.list.append(values)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.list.pop()

    def peek(self):
        if self.list.isEmpty():
            return "Stack is Empty"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


# Space and time complexity : O(1)
