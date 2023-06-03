from queue import PriorityQueue

from egzP8btesty import runtests


def robot( G, P ):
    #print(G)
    #print(P)
    #print(Djikstra(G, P[0]))

    suma = 0
    for i in range(1, len(P)):
        start = i - 1
        end = i

        suma += Djikstra(G, P[start])[P[end]]


    #Tutaj proszę wpisać własną implementację
    return suma

def deleteVerticle(G, idx):
    newG = [[] for _ in range(len(G))]

    for i in range(len(G)):
        if i not in idx:
            for j in range(len(G[i])):
                if G[i][j] not in idx:
                    newG[i].append(G[i][j])
    return newG
def Djikstra(G, s):  # dla list sąsiedztwa G[v]: pary [u, w(v, u)] ->  O(V+E)
    PQ = PriorityQueue()

    visited = [False] * len(G)
    parent = [None] * len(G)
    d = [float('inf')] * len(G)
    d[s] = 0

    PQ.put((0, s))
    while not PQ.empty():
        _, v = PQ.get()
        if not visited[v]:
            for u, w in G[v]:
                if not visited[u]:
                    if d[u] > d[v] + w:
                        d[u] = d[v] + w
                        parent[u] = v
                        PQ.put((d[u], u))
            visited[v] = True
    return d
runtests(robot, all_tests = True)
