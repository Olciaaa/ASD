class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def findMaximum(root):
    while root.right:
        root = root.right
    return root

def findPredecessor(root, prec, key):
    if root is None:
        return prec

    if root.data == key:
        if root.left:
            return findMaximum(root.left)

    elif key < root.data:
        return findPredecessor(root.left, prec, key)

    else:
        prec = root
        return findPredecessor(root.right, prec, key)

    return prec

#findPredecessor(root, None, key)
