import Queue_here.LinkedListQ as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.LeftChild = None
        self.RightChild = None
        # Time Complexity : O(1)


node = TreeNode("Drinks")
LeftChild = TreeNode("Hot")
RightChild = TreeNode("Cold")
node.LeftChild = LeftChild
node.RightChild = RightChild

print("----- PreOrder -----")


def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.LeftChild)  # Time Complexity : O(n/2)
    preOrder(rootNode.RightChild)  # Time Complexity : O(n)


preOrder(node)

print("----- InOrder -----")


def inOrder(rootNode):
    if not rootNode:
        return

    inOrder(rootNode.LeftChild)
    print(rootNode.data)
    inOrder(rootNode.RightChild)


inOrder(node)

print("----- PostOrder -----")


def PostOrder(rootNode):
    if not rootNode:
        return

    PostOrder(rootNode.LeftChild)
    PostOrder(rootNode.RightChild)
    print(rootNode.data)


PostOrder(node)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return False
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Sucess"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not found"


print("Searching in a Binary tree")
print(searchBT(node, "Tea"))
