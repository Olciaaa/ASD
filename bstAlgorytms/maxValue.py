def maxValue(root):
    current = root

    while (current.right):
        current = current.right
    return current.data