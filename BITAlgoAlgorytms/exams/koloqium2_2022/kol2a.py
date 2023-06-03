from queue import PriorityQueue

from kol2atesty import runtests

def drivers( P, B ):
    #print(P)
    # tu prosze wpisac wlasna implementacje
    P.sort(key = lambda x: x[0])
    G = makeGraph(P)
    #print(G)
    results, parents = Dijkstra(G, 0)
    #print(parents)
    print(min(results[0][len(results[0]) - 1], results[1][len(results[1]) - 1]))
    return []

def makeGraph(P):
    values = []
    values.append(0)
    controlPointsGathered = 0
    for el in P:
        if not el[1]:
            controlPointsGathered += 1
        else:
            values.append(controlPointsGathered)
            controlPointsGathered = 0
    #print(values)

    G = [[] for _ in range(len(values))]
    for i in range(len(values)):
        val = 0
        for j in range(1, 4):
            if i + j < len(values):
                val += values[i + j]
                G[i].append((i + j, val))
                G[i + j]. append((i, val))
    return G
def Dijkstra(G, s):
    #0 Jacek, 1 Marek
    d = [[float('inf') for _ in range(len(G))] for _ in range(2)]
    parent = [[-1 for _ in range(len(G))] for _ in range(2)]
    visited = [[False for _ in range(len(G))] for _ in range(2)]

    q = PriorityQueue()
    d[1][s] = 0
    q.put((0, s, 1))

    while not q.empty():
        _, u, flag = q.get()
        if not visited[flag][u]:
            for v, value in G[u]:
                if not visited[(flag + 1) % 2][v]:
                    relax(flag, d, parent, u, v, value * ((flag + 1) % 2))
                    q.put((d[(flag + 1) % 2][v], v, (flag + 1) % 2))
        visited[flag][u] = True

    return d, parent

def relax(flag, d, parent, u, v, value):
    #flag = M, u = dla Marka, v jest dla Jacka
    if d[(flag + 1) % 2][v] > d[flag][u] + value:
        d[(flag + 1) % 2][v] = d[flag][u] + value
        parent[(flag + 1) % 2][v] = u

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )