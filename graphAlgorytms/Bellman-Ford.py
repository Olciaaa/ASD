from math import inf


def BellmanFord(G, V, s):  # graf reprezentowany listą krawędzi, V to liczba wierzchołków w grafie
    parent = [None] * V
    d = [inf] * V
    d[s] = 0
    for _ in range(V - 1):
        for edge in G:
            u, v, w = edge
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                parent[v] = u

    check = False  # czy istnieją ujemne cykle
    for edge in G:
        u, v, w = edge
        if d[v] > d[u] + w:
            check = True
            break

    return check, d, parent