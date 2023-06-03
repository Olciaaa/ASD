'''
Aleksandra Poskróbek

Mój pomysł polega na tym, że najpierw tworzę posortowaną po długościach odcinków listę połączeń między wierzchołkami,
po której następnie chodzę dwoma "znacznikami" i szukam listy takich spójnych połączeń, które mają najmniejszą różnicę
między najmniejszym i największym odcinkiem.
'''

from zad8testy import runtests

def addConnection(G, connectionToAdd, counter, numOfConnVert):
    if G[connectionToAdd[1]] == G[connectionToAdd[2]] and G[connectionToAdd[1]] is not None:
        return (counter, numOfConnVert)

    if G[connectionToAdd[1]] is None and G[connectionToAdd[2]] is None:
        if counter == 0: numOfConnVert += 2
        G[connectionToAdd[1]] = G[connectionToAdd[2]] = counter
        counter += 1
    elif G[connectionToAdd[1]] is not None and G[connectionToAdd[2]] is None:
        if G[connectionToAdd[1]] == 0: numOfConnVert += 1
        G[connectionToAdd[2]] = G[connectionToAdd[1]]
    elif G[connectionToAdd[2]] is not None and G[connectionToAdd[1]] is None:
        if G[connectionToAdd[2]] == 0: numOfConnVert += 1
        G[connectionToAdd[1]] = G[connectionToAdd[2]]
    else:
        p = 0
        if G[connectionToAdd[2]] > G[connectionToAdd[1]]:
            comp = G[connectionToAdd[2]]
            for i in range(len(G)):
                if G[i] == comp:
                    G[i] = G[connectionToAdd[1]]
                    p += 1
            if G[connectionToAdd[1]] == 0: numOfConnVert += p
        else:
            comp = G[connectionToAdd[1]]
            for i in range(len(G)):
                if G[i] == comp:
                    G[i] = G[connectionToAdd[2]]
                    p += 1
            if G[connectionToAdd[2]] == 0: numOfConnVert += p

    return (counter, numOfConnVert)

def highway( A ):
    if len(A) == 1: return 0
    if len(A) == 2: return ceil(((A[1][0] - A[0][0]) ** 2 + (A[1][1] - A[0][1]) ** 2) ** 0.5)

    sortedLengths = listOfLengths(A)

    minimum = float('inf')
    G = [None for _ in range(len(A))]

    i = 0
    j = 0
    counter = 0
    numOfConnVert = 0

    while j < len(sortedLengths):
        lastEl = sortedLengths[j]
        firstEl = sortedLengths[i]
        currentLen = lastEl[0] - firstEl[0]

        counter, numOfConnVert = addConnection(G, lastEl, counter, numOfConnVert)

        if numOfConnVert == len(A):
            minimum = min(currentLen, minimum)

            i += 1
            G = [None for _ in range(len(A))]
            counter = 0
            numOfConnVert = 0

            for k in range(j, i - 1, -1):
                counter, numOfConnVert = addConnection(G, sortedLengths[k], counter, numOfConnVert)
                if numOfConnVert == len(A):
                    i = k
                    break
        else:
            j += 1
    return minimum

def ceil(number):
    num = int(number)
    if num == number: return num
    return num + 1

def listOfLengths(A):
    tab = []

    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            length = ceil(((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** 0.5)
            tab.append((length, i, j))
    tab.sort(key=lambda x: (x[0]))

    return tab

runtests( highway, all_tests = True )