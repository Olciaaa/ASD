from math import inf

from egzP4btesty import runtests

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None


def sol(root, T):
  suma = 0
  for el in T:
    node = findEl(root, el.key)

    #print(f"node: {node.key}")
    #print(f"less: {findLessMax(node)}")
    #print(f"gross: {findGrossMin(node)}")
    if (findLessMax(node) + findGrossMin(node))/2 == node.key:
      suma += node.key
  return suma

def findEl(current, value):
  if current.key == value: return current

  elif current.key < value:
    return findEl(current.right, value)
  else:
    return findEl(current.left, value)

def findLessMax(current):
  if current.left is None:
    childCurr = current
    current = current.parent
    while current.parent is not None and current.right != childCurr:
      childCurr = current
      current = current.parent
  else:
    current = current.left
    while current.right is not None:
      current = current.right

  return current.key

def findGrossMin(current):
  if current.right is None:
    childCurr = current
    current = current.parent
    while current.parent is not None and current.left != childCurr:
      childCurr = current
      current = current.parent
  else:
    current = current.right
    while current.left is not None:
      current = current.left

  return current.key
    
runtests(sol, all_tests = True)