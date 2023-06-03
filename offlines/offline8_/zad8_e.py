from queue import Queue
from zad8testy import runtests

def isConnected(n, G):
    for el in G:
        if not el: return False

    counter = 0
    visited = [False for _ in range(len(G))]
    q = Queue()
    q.put(0)
    visited[0] = True

    while not q.empty():
        s = q.get()
        counter += 1

        for i in range(len(G[s])):
            if not visited[G[s][i]]:
                q.put(G[s][i])
                visited[G[s][i]] = True
    return n == counter

def highway( A ):
    print(A)
    sortedLengths = listOfLengths(A)

    #print(sortedLengths)

    minimum = float('inf')
    verticles = [[] for _ in range(len(A))]

    i = 0
    j = 0

    while j < len(sortedLengths):
        lastEl = sortedLengths[j]
        firstEl = sortedLengths[i]
        currentLen = lastEl[0] - firstEl[0]

        if lastEl[2] not in verticles[lastEl[1]]:
            verticles[lastEl[1]].append(lastEl[2])

        if lastEl[1] not in verticles[lastEl[2]]:
            verticles[lastEl[2]].append(lastEl[1])

        if isConnected(len(A), verticles):
            minimum = min(currentLen, minimum)

            verticles[firstEl[1]].remove(firstEl[2])
            verticles[firstEl[2]].remove(firstEl[1])
            i += 1
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