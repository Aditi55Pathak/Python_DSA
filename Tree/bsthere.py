class BSTTree:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.value == None:
        rootNode.value = nodeValue
    elif nodeValue <= rootNode.value:
        if rootNode.leftChild == None:
            rootNode.leftChild = BSTTree(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild == None:
            rootNode.rightChild = BSTTree(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "Value inserted successfully!!"


def preOrderTraversal(rootNode):  # ---------> O(n)
    if not rootNode:
        return
    print(rootNode.value)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):  # ---------> O(n)
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.value)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):  # ---------> O(n)
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.value)


# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not(customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             print(root.value.data)
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)


def searchBst(rootNode, nodeValue):
    if rootNode.value == nodeValue:
        print("Data element is found!!")
    elif nodeValue < rootNode.value:
        if rootNode.leftChild.value == nodeValue:
            print("Data element is found!!")
        else:
            searchBst(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.value == nodeValue:
            print("Data element is found!!")
        else:
            searchBst(rootNode.rightChild, nodeValue)


def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"


bst = BSTTree(None)
insertNode(bst, 70)
insertNode(bst, 90)
insertNode(bst, 9)
insertNode(bst, 23)
insertNode(bst, 60)
print("----PreOrder----")
preOrderTraversal(bst)
print("----InOrder----")
inOrderTraversal(bst)
print("----PostOrder----")
postOrderTraversal(bst)
print("*** Searching for elements *** ")
searchBst(bst, 60)
