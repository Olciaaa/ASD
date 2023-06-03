from math import inf

from egzP1atesty import runtests

def titanic( W, M, D ):
    word = makeWord(W, M)
    dynamic = [-1 for _ in range(len(word) + 1)]
    for i in range(len(D)):
        #print(D[i])
        D[i] = M[D[i]][1]
    #print(D)
    result = howMany(word, D, dynamic, 0)
    print(dynamic)
    return result
    #tutaj proszę wpisać własną implementację

def makeWord(W, M):
    word = ""
    for i in range(len(W)):
        charNum = ord(W[i]) - 65
        word += M[charNum][1]

    return word

def howMany(word, D, dynamic, idx):
    if len(word) == idx:
        dynamic[idx] = 0
        return 0

    if dynamic[idx] != -1: return dynamic[idx]

    minimum = inf
    for el in D:
        if el == word[idx:len(el) + idx]:
            minimum = min(minimum, howMany(word, D, dynamic, idx + len(el)))
    dynamic[idx] = minimum + 1
    return minimum + 1

runtests ( titanic, recursion=True )