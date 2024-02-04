class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChildren(self, child):
        self.children.append(child)


tree = TreeNode("Drinks", [])
cold = TreeNode("Cold Drinks")
hot = TreeNode("Hot Drinks")
tree.addChildren(cold)
tree.addChildren(hot)

tea = TreeNode("Black")
coffee = TreeNode("Coffee")
fanta = TreeNode("Fanta")
Coke = TreeNode("Coke")
hot.addChildren(tea)
hot.addChildren(coffee)
cold.addChildren(fanta)
cold.addChildren(Coke)

print(tree)
