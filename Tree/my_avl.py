class AvlTree:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def insertNode(rootNode, nodeValue):
    if rootNode.value == None:
        rootNode.value = nodeValue
    elif nodeValue <= rootNode.value:
        if rootNode.leftChild == None:
            rootNode.leftChild = AvlTree(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild == None:
            rootNode.rightChild = AvlTree(nodeValue)
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


def searchAvl(rootNode, nodeValue):
    if rootNode.value == nodeValue:
        print("Data element is found!!")
    elif nodeValue < rootNode.value:
        if rootNode.leftChild.value == nodeValue:
            print("Data element is found!!")
        else:
            searchAvl(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.value == nodeValue:
            print("Data element is found!!")
        else:
            searchAvl(rootNode.rightChild, nodeValue)


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


def deleteAvl(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"


def getHeight(rootNode):
    if rootNode == None:
        return 0
    return rootNode.height


def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(
        getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
    )
    return newRoot


def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(
        getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
    )
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    else:
        return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AvlTree(nodeValue)
    elif nodeValue < rootNode.value:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(
        getHeight(rootNode.leftChild), getHeight(rootNode.rightChild)
    )
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.value:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.value:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.value:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.value:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


avl = AvlTree(None)
insertNode(avl, 70)
insertNode(avl, 90)
insertNode(avl, 9)
insertNode(avl, 23)
insertNode(avl, 60)
print("----PreOrder----")
preOrderTraversal(avl)
print("----InOrder----")
inOrderTraversal(avl)
print("----PostOrder----")
postOrderTraversal(avl)
print("*** Searching for elements *** ")
searchAvl(avl, 60)

newAVL = AvlTree(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
