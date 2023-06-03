# The Ford-Fulkerson algorithm is a greedy algorithm that computes the maximum flow in a flow network (G).
from math import inf
from random import randint


def dfs_visit(G, V, P, i):
    V[i] = True
    for nb in range(len(G)):
        if not V[nb] and G[i][nb] != 0:
            P[nb] = i
            dfs_visit(G, V, P, nb)


def dfs(G, s, t, P):
    V = [False for _ in range(len(G))]
    dfs_visit(G, V, P, s)
    return V[t]


def fordFulkersonMatrix(G, s, t):
    P = [None for _ in range(len(G))]
    max_flow = 0
    while dfs(G, s, t, P):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, G[P[current]][current])
            current = P[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = P[v]
            G[u][v] -= current_flow
            G[v][u] += current_flow
            v = P[v]
    return max_flow