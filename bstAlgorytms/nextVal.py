class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def inOrderSuccessor(n):
    if n.right is not None:
        return minValue(n.right)

    p = n.parent
    while (p is not None):
        if n != p.right:
            break
        n = p
        p = p.parent
    return p

def minValue(node):
    current = node

    while (current is not None):
        if current.left is None:
            break
        current = current.left

    return current