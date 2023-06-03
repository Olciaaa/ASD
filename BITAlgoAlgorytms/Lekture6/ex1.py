#Napisz algorytm sprawdzający, czy graf nieskierowany posiada cykl.
visited = []
parent = []
flag = False

def isCycled(G):
    global visited, flag, parent
    flag = False
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]

    for v in range(len(G)):
        if not visited[v]:
            dfsVisit(G, v)

    return flag

def dfsVisit(G, u):
    global visited, flag, parent
    visited[u] = True

    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            dfsVisit(G, v)
        else:
            if parent[u] != v: flag = True

G1 = [[1], [0, 2, 4, 5], [1, 3], [2], [1, 5], [1, 4]]
G2 = [[1], [0, 2, 4], [1, 3], [2], [1, 5], [4]]

print(isCycled(G1))
print(isCycled(G2))
