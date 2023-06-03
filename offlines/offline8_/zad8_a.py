from queue import Queue
from zad8testy import runtests

def addConnection(G, connection):
    G[connection[1]][connection[2]] = True
    G[connection[2]][connection[1]] = True

    for i in range(len(G)):
        if G[connection[1]][i]:
            G[connection[2]][i] = True
            G[i][connection[2]] = True
        if G[i][connection[2]]:
            G[i][connection[1]] = True
            G[connection[1]][i] = True
def isConnected(G):
    for i in range(len(G)):
        if not G[0][i]: return False
    return True

def highway( A ):
    print(len(A))
    sortedLengths = listOfLengths(A)
    print(sortedLengths)

    minimum = float('inf')
    connections = [[False for _ in range(len(A))] for _ in range(len(A))]

    i = 0
    j = 0

    while j < len(sortedLengths):
        lastEl = sortedLengths[j]
        firstEl = sortedLengths[i]
        currentLen = lastEl[0] - firstEl[0]

        addConnection(connections, lastEl)

        if isConnected(connections):
            minimum = min(currentLen, minimum)
            i += 1
            connections = [[False for _ in range(len(A))] for _ in range(len(A))]
            for k in range(i, j + 1):
                addConnection(connections, sortedLengths[k])
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

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )