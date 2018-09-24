# Bitch what the fuck

#Node class for Binary Tree
class Node:
    def __init__(self, val):
        self.left = null
        self.right = null
        self.value = val

# Lowest Common Ancestor - find lowest common ancester of x and y
def LCA(node, x, y):
    if node == None:
        return None
    if node == x or node == y:
        return node
    left = LCA(node.left, x, y)
    right = LCA(node.right, x, y)
    if left == None:
        return right
    else:
        return left
