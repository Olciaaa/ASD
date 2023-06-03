from math import inf
from egzP1atesty import runtests

def titanic( W, M, D ):
    word = makeWord(W, M)
    dynamic = [-1 for _ in range(len(word) + 1)]
    #print(D)
    result = howMany(M, word, D, dynamic, 0)
    print(dynamic)
    return result
    #tutaj proszę wpisać własną implementację

def makeWord(W, M):
    word = ""
    for i in range(len(W)):
        charNum = ord(W[i]) - 65
        word += M[charNum][1]

    return word

def bin(value, data):
    left = 0
    right = len(data) - 1

    while left < right:
        middle = (left + right)//2
        if data[middle] < value:
            left = middle + 1
        else: right = middle
    if data[right] == value:
        return right
    else: return None

def howMany(M, word, D, dynamic, idx):
    if len(word) == idx:
        dynamic[idx] = 0
        return 0

    if dynamic[idx] != -1: return dynamic[idx]

    minimum = inf

    for i in range(1, 5):
        if idx + i >= len(word): break
        el = word[idx:idx + i]
        if bin(el, D) != None:
            minimum = min(minimum, howMany(M, word, D, dynamic, idx + i))

    dynamic[idx] = minimum + 1
    return minimum + 1

runtests ( titanic, recursion=True )