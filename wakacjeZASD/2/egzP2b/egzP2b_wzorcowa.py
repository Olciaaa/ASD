import time

from egzP2btesty import runtests
from math import log10
class bst:
    def __init__(self, left, right, value, key):
        self.left = left
        self.right = right
        self.value = value
        self.parent = None
        self.key = key
        self.children = 0
    def __str__(self):
        return f"left: {self.left is not None}, right: {self.right is not None}, value: {self.value}, children: {self.children}"

def countingSort(tab, idx):
    C = [0 for _ in range(2)]
    B = [0 for _ in range(len(tab))]

    for el in tab:
        C[int(el[0][idx])] += 1
    for i in range(1, 2):
        C[i] = C[i] + C[i-1]
    for i in range(len(tab)-1, -1, -1):
        B[C[int(tab[i][0][idx])] - 1] = tab[i]
        C[int(tab[i][0][idx])] -= 1
    for i in range(len(tab)):
        tab[i] = B[i]

def radix(D):
    maxLen = 0
    for el in D:
        if maxLen < len(el):
            maxLen = len(el)

    for idx in range(len(D)):
        D[idx] = [D[idx], D[idx], len(D[idx])]

    for idx in range(len(D)):
        for i in range(len(D[idx][0]), maxLen):
            D[idx][0] = "0" + D[idx][0]
    D.sort(key = lambda x: x[2])

    for i in range(maxLen):
        countingSort(D, i)

def binToDec(data):
    dataValue = 0
    pover = 0
    for i in range(len(data) - 1, -1, -1):
        dataValue += int(data[i]) * (2 ** pover)
        pover += 1
    return dataValue

def makeTree(D):
    root = bst(None, None, "", False)
    current = root

    for key, el, i in D:
        n = len(el) - len(current.value)
        while current != root and current.value != el[n:len(el)]:
            current = current.parent
            n += 1

        while n != 0:
            n -= 1
            key = False
            if n == 0:
                key = True
            elementToAdd = bst(None, None, el[n:len(el)], key)
            elementToAdd.parent = current
            if el[n:n+1] == "0":
                current.left = elementToAdd
            else:
                current.right = elementToAdd
            current = elementToAdd

    return root

def readTree(root):
    if root is not None:
        print(root)
        readTree(root.left)
        readTree(root.right)

def countChildren(current):
    suma = 0
    if current.left is not None:
        suma += countChildren(current.left)
        if current.left.key: suma += 1
    if current.right is not None:
        suma += countChildren(current.right)
        if current.right.key: suma += 1
    current.children = suma
    return suma

def find(current, el):
    if current.value == el:
        val = 0
        if current.key: val = 1
        return current.children + val
    if el[len(el) - len(current.value) - 1] == "1":
        return find(current.right, el)
    if el[len(el) - len(current.value) - 1] == "0":
        return find(current.left, el)

def kryptograf( D, Q ):
    #tutaj proszę wpisać własną implementację
    start1 = time.time()
    radix(D)
    end1 = time.time()
    #print(D)
    start2 = time.time()
    root = makeTree(D)
    end2 = time.time()
    #readTree(root)
    toReturn = 0
    start3 = time.time()
    countChildren(root)
    end3 = time.time()
    start4 = time.time()
    #readTree(root)
    for el in Q:
        #print(f"{el}, {find(root, el, False)}")
        if len(el) == 0:
            toReturn += log10(len(D))
        elif el[len(el) - 1] == "0":
            toReturn += log10(find(root.left, el))
        else:
            toReturn += log10(find(root.right, el))
    end4 = time.time()

    print(f"1: {end1 - start1}, 2: {end2 - start2}, 3: {end3 - start3}, 4: {end4 - start4}")
    #print(toReturn)
    return toReturn

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 3)
D = ['0', '100', '1100', '1101', '1111']
Q = ['', '1', '11', '0', '1101']
#kryptograf(D, Q)