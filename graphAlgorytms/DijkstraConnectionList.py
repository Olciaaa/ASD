from queue import PriorityQueue

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
    return d, parent

G = [[(1,3), (4,3)], [(2, 1)], [(3, 3), (5, 1)], [(1, 3)], [(5, 2)], [(0, 6), (3, 1)]]
print(Djikstra(G, 0))
