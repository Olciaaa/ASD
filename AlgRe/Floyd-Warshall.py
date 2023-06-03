def Floyd_Warshall(G):
    n = len(G)

    Dist = [[float('inf') for i in range(n)] for j in range(n)]
    parent = [[None for i in range(n)] for j in range(n)]

    for u in range(n):
        for v in G[u]:
            Dist[u][v[0]] = v[1]
            parent[u][v[0]] = v[0]
    
    for v in range(n):
        Dist[v][v] = 0
        parent[v][v] = v

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if Dist[u][v] > Dist[u][k] + Dist[k][v]:
                    Dist[u][v] = Dist[u][k] + Dist[k][v]
                    parent[u][v] = parent[u][k]
    
    return Dist, parent

def path(parent, u,v):

    if matrix[u][v] == None:
        return None
    res = [u]

    while u != v:
        u = parent[u][v]
        res.append(u)

    return res


graph = [
    [(1, 1)],
    [(0, 1), (2, 2), (3, 3)],
    [(1, 2), (3, 1), (4, 5)],
    [(1, 3), (2, 1), (4, 1)],
    [(2, 5), (3, 1)]
]

matrix, parent = Floyd_Warshall(graph)

for i in range(len(matrix)):
    print(matrix[i])

u = 1
v = 4

print(path(parent,u,v))
