'''
Algorytm opiera się na stworzeniu z tablicy S i G grafu zapisanego na liście z połączeniami wierzchołków i wagami. Następnie
wykonuję algorytm Dijkstry i znajduję najkrótszą ścieżkę jaką może pokonać ktosiek z planety a do planety b.

Algorytm ma złożoność O((długości tablicy G * 2 +  długość tablicy S ^ 2 * 2) + mlogn)

'''

from queue import PriorityQueue

from kol3atesty import runtests

dist = []
parent = []
visited = []
used = []

def spacetravel(n, E, S, a, b):
    global dist, parent

    G = makeGraph(E, S, n)
    dijkstra(G, a)
    #print(G)
    #print(parent)
    #print(dist)
    if dist[b] == float('inf'): return None
    return dist[b]


def makeGraph(E, S, n):
    G = [[] for _ in range(n)]

    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))

    verticle = []
    for idx in range(len(S)):
        for jdx in range(idx + 1, len(S)):
            #print(S[idx], " ", S[jdx])
            G[S[idx]].append((S[jdx], 0))
            G[S[jdx]].append((S[idx], 0))
    return G

def dijkstra(G, start):
    global visited, used, dist, parent

    n = len(G)
    q = PriorityQueue()
    visited = [False for _ in range(n)]
    used = [False for _ in range(n)]
    dist = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]

    dist[start] = 0
    q.put((0, start))
    used[start] = True

    while not q.empty():
        key, u = q.get()
        visited[u] = True

        for el in G[u]:
            v, payment = el
            if not visited[v]:
                relax(u, v, payment, q)

            if not used[v]:
                used[v] = True
                q.put((dist[v], v))

def relax(u, v, payment, q):
    global dist, parent
    if dist[v] > dist[u] + payment:
        dist[v] = dist[u] + payment
        parent[v] = u

#tylko to:
        if used[v]:
            q.put((dist[v], v))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
