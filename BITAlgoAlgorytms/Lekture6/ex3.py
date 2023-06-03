'''Dana jest dwuwymiarowa tablica N x N, w której każda komórka ma wartość “W” - reprezentującą wodę lub “L” - ląd.
Grupę komórek wody połączonych ze sobą brzegami nazywamy jeziorem.

a)Policz, ile jezior jest w tablicy

b)Policz, ile komórek zawiera największe jezioro

c) Zakładając, że pola o indeksach [0][0] i [n-1][n-1] są lądem, sprawdź czy da się przejść drogą lądową z pola [0][0]
do pola [n-1][n-1]. Można chodzić tylko na boki, nie na ukos.

d) Znajdź najkrótszą ścieżkę między tymi punktami. Wypisz po kolei indeksy pól w tej ścieżce
'''
from queue import Queue

visited = []
parent = []
currRiver = 0

def LakeAnswers(matrix):
    GW = makeGraphWater(matrix)
    GL = makeGraphLand(matrix)

    lenPath, parents = bfs(GL, 0, len(GW) - 1)
    tab = []

    i = len(parents) - 1
    if not lenPath == None:
        while i >= 0:
            tab.append((i // len(matrix), i % len(matrix)))
            i = parents[i]
        tab = tab[::-1]

    return dfs(GW, matrix), not lenPath == None, tab

def bfs(G, s, e):
    visited = [False for _ in range(len(G))]
    distanceFromS = [0 for _ in range(len(G))]
    parents = [-1 for _ in range(len(G))]
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        s = q.get()

        if s == e: return distanceFromS[s], parents

        for i in range(len(G[s])):
            if not visited[G[s][i]]:
                parents[G[s][i]] = s
                q.put(G[s][i])
                visited[G[s][i]] = True
                distanceFromS[G[s][i]] = distanceFromS[s] + 1
    return None, []

def dfs(G, matrix):
    global visited, parent, currRiver
    riverCount = 0
    biggestRiver = 0
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]

    for i in range(len(G)):
        if not visited[i]:
            currRiver = 0
            if matrix[i // len(matrix)][i % len(matrix)] == 'W': riverCount += 1
            dfsVisit(G, i)
            biggestRiver = max(biggestRiver, currRiver)

    return riverCount, biggestRiver

def dfsVisit(G, u):
    global visited, parent, currRiver
    visited[u] = True

    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            dfsVisit(G, v)
    currRiver += 1


def makeGraphWater(matrix):
    n = len(matrix)
    G = [[] for _ in range(n ** 2)]

    for i in range(n):
        for j in range(n):
            verticleNum = i * n + j
            if matrix[i][j] == 'W':
                if i - 1 >= 0 and matrix[i - 1][j] == 'W':
                    G[verticleNum].append(verticleNum - n)
                if i + 1 < n and matrix[i + 1][j] == 'W':
                    G[verticleNum].append(verticleNum + n)
                if j - 1 >= 0 and matrix[i][j - 1] == 'W':
                    G[verticleNum].append(verticleNum - 1)
                if j + 1 < n and matrix[i][j + 1] == 'W':
                    G[verticleNum].append(verticleNum + 1)

    return G
def makeGraphLand(matrix):
    n = len(matrix)
    G = [[] for _ in range(n ** 2)]

    for i in range(n):
        for j in range(n):
            verticleNum = i * n + j
            if matrix[i][j] == 'L':
                if i - 1 >= 0 and matrix[i - 1][j] == 'L':
                    G[verticleNum].append(verticleNum - n)
                if i + 1 < n and matrix[i + 1][j] == 'L':
                    G[verticleNum].append(verticleNum + n)
                if j - 1 >= 0 and matrix[i][j - 1] == 'L':
                    G[verticleNum].append(verticleNum - 1)
                if j + 1 < n and matrix[i][j + 1] == 'L':
                    G[verticleNum].append(verticleNum + 1)

    return G

matrix = [
    ['L', 'W', 'L', 'L', 'L', 'L', 'L', 'L'],
    ['L', 'W', 'L', 'W', 'W', 'L', 'L', 'L'],
    ['L', 'L', 'L', 'W', 'W', 'L', 'W', 'L'],
    ['L', 'W', 'W', 'W', 'W', 'L', 'W', 'L'],
    ['L', 'L', 'W', 'W', 'L', 'L', 'L', 'L'],
    ['L', 'W', 'L', 'L', 'L', 'L', 'W', 'W'],
    ['W', 'W', 'L', 'W', 'W', 'L', 'W', 'L'],
    ['L', 'L', 'L', 'W', 'L', 'L', 'L', 'L'],
    ]
matrix = [
        ["W", "L", "W", "L", "W"],
        ["L", "W", "L", "W", "L"],
        ["W", "L", "W", "L", "W"],
        ["L", "W", "L", "W", "L"],
        ["W", "L", "W", "L", "W"]
    ]
print(LakeAnswers(matrix))