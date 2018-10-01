# LCA.py

#Node class for Binary Tree
class Node:
    #Init
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    #Print the Binary Tree to console
    def print_tree(self):
        if self.left != None:
            self.left.print_tree()
        print(self.value)
        if self.right != None:
            self.right.print_tree()

# Lowest Common Ancestor - find lowest common ancester of x and y using recursion
def LCA(node, x, y):
    if node is None:
        return None

    if node.value == x or node.value == y:
        return node

    left = LCA(node.left, x, y)
    right = LCA(node.right, x, y)

    if left != None and right != None:
        return node

    if left == None:
        return right
    else:
        return left

#Create Binary Tree for testing
testTree = Node(1)
testTree.left = Node(2)
testTree.right = Node(3)
testTree.left.left = Node(8)
testTree.left.right = Node(7)
testTree.left.right.left = Node(9)
testTree.left.right.right = Node(10)
testTree.right.left = Node(4)
testTree.right.right = Node(5)
testTree.right.right.right = Node(6)
