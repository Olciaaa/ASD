from queue import PriorityQueue

from egzP1btesty import runtests

def turysta( G, D, L ):
    n = 0

    for el in G:
        if el[0] > n: n = el[0]
        if el[1] > n: n = el[1]

    Graph = [[] for _ in range(n + 1)]

    for el in G:
        Graph[el[0]].append((el[1], el[2]))
        Graph[el[1]].append((el[0], el[2]))

    #print(Graph)
    d, parents = Djikstra(Graph, D)
    #print(d)
    #print(parents)
    #print(d[4][L])
    #tutaj proszę wpisać własną implementację
    return d[4][L]

def Djikstra(G, s):
    PQ = PriorityQueue()

    visited = [[False for _ in range(len(G))]for _ in range(5)]
    parent = [[None for _ in range(len(G))] for _ in range(5)]
    d = [[float('inf') for _ in range(len(G))] for _ in range(5)]
    d[0][s] = 0

    PQ.put((0, s, 0))
    while not PQ.empty():
        _, v, distance = PQ.get()
        if distance < 4 and not visited[distance][v]:
            for u, w in G[v]:
                if not visited[distance + 1][u]:
                    if d[distance + 1][u] > d[distance][v] + w:
                        d[distance + 1][u] = d[distance][v] + w
                        parent[distance + 1][u] = v
                        PQ.put((d[distance + 1][u], u, distance + 1))
            visited[distance][v] = True
    return d, parent

runtests ( turysta )