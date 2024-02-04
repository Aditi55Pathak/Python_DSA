class Multistack:
    def __init__(self, StackSize):
        self.numberstacks = 3
        self.custlist = [0] * (StackSize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.StackSize = StackSize

    def isFull(self, StackNum):
        if self.sizes[StackNum] == self.StackSize:
            return True
        else:
            return False

    def isEmpty(self, StackNum):
        if self.sizes[StackNum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, StackNum):
        offset = StackNum * self.StackSize
        return offset + self.sizes[StackNum] - 1

    def push(self, item, StackNum):
        if self.isFull(StackNum):
            return "Stack is Full"
        else:
            self.sizes[StackNum] += 1
            self.custlist[self.indexOfTop(StackNum)] = item

    def pop(self, StackNum):
        if self.isEmpty(StackNum):
            value = self.custlist[self.indexOfTop(StackNum)]
            self.custlist[self.indexOfTop(StackNum)] = 0
            self.sizes[StackNum] -= 1
            return value

    def peek(self, StackNum):
        if self.isEmpty(StackNum):
            value = self.custlist[self.indexOfTop(StackNum)]
            return value


myStack = Multistack(6)
print(myStack.isFull(1))
print(myStack.isEmpty(0))
myStack.push(0, 1)
myStack.push(1, 0)
myStack.push(2, 1)
print(myStack.peek(2))
