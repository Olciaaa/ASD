def Djikstra2(G, s):  # dla reprezentacji macierzowej G[v][u] = w(v, u) -> O(V**2)

    def min_index(n):
        nonlocal visited, d
        min_ = float('inf')
        index = -1
        for i in range(n):
            if not visited[i] and d[i] < min_:
                index = i
                min_ = d[i]
        return index

    n = len(G)
    visited = [False] * n
    parent = [None] * n
    d = [float('inf')] * n
    d[s] = 0

    for _ in range(n):  # bo bierzemy n wierzchołków w sumie
        u = min_index(n)
        for v in range(n):
            if not visited[v]:
                if G[u][v] > 0 and d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]
                    parent[v] = u
        visited[u] = True
    return d, parent