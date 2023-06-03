from math import inf


def Floyd_Warshall(G):
    n = len(G)
    T = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                T[i][j] = G[i][j]
            if i == j:
                T[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = min(T[i][j], T[i][k] + T[k][j])

    return T
