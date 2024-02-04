class binaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertHere(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "Value has been inserted sucessfully"

    def searchHere(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "AanSuccess"

    def preOrder(self, index):
        if index > self.lastUsedIndex:
            return 0
        print(self.customList[index])
        self.preOrder(index * 2)  # time Complexity : O(n/2)----> O(n)
        self.preOrder(index * 2 + 1)  # time Complexity : O(n/2)----> O(n)

    def inOrder(self, index):
        if index > self.lastUsedIndex:
            return 0
        self.inOrder(index * 2)  # time Complexity : O(n/2)----> O(n)
        print(self.customList[index])
        self.inOrder(index * 2 + 1)  # time Complexity : O(n/2)----> O(n)

    def postOrder(self, index):
        if index > self.lastUsedIndex:
            return 0
        self.postOrder(index * 2)  # time Complexity : O(n/2)----> O(n)
        self.postOrder(index * 2 + 1)  # time Complexity : O(n/2)----> O(n)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(
            index, self.lastUsedIndex + 1
        ):  # time Complexity : O(n/2)----> O(n)
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] == self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The Node has been deleted sucessfully!!"

    def DeleteEntire(self):
        self.customList = None
        return "Entire Tree deleted!!"


newBT = binaryTree(6)
newBT.insertHere("Drinks")
newBT.insertHere("Hot")
newBT.insertHere("Cold")
newBT.insertHere("tea")
newBT.insertHere("Cola")
print("------Searching node Here -------")
print(newBT.searchHere("Hot"))
print(newBT.searchHere("Ammino"))
print("----PreOrder----")
newBT.preOrder(1)
print("----inOrder----")
newBT.inOrder(1)
print("----PostOrder----")
newBT.postOrder(1)
print("---- Level Order Traversal ----")
newBT.levelOrderTraversal(1)
print("----Delete----")
print(newBT.deleteNode("tea"))
newBT.levelOrderTraversal(1)
print("----Delete Entire Tree----")
print(newBT.DeleteEntire())
