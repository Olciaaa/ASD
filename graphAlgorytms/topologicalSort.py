from queue import Queue
list = []

def dfs(G):
    global visited
    visited = [False for _ in range(len(G))]

    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx)

def dfsVisit(G, s):
    global visited, list
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            dfsVisit(G, el)
    list.append(s)

def topologicalSort(G):
    global list
    dfs(G)

    for i in range(len(list) - 1, -1, -1):
        print(list[i])

G = [[2], [0, 2], [], [0, 1, 4], [1, 2], [0, 4]]
topologicalSort(G)
