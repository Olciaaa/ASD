from math import inf
from queue import PriorityQueue

from egzP7atesty import runtests

def akademik( T ):
    G = makeGraph(T)

    studentsWithNoNeeds = 0
    for el in T:
        if el[0] == el[1] == el[2] and el[0] is None:
            studentsWithNoNeeds += 1

    return len(T) - fordFulkerson(G, 0, len(G) - 1) - studentsWithNoNeeds

def makeGraph(T):
    G = [[] for _ in range(len(T) * 2 + 2)]

    for i in range(1, len(T) + 1):
        G[0].append(i)

    for i in range(len(T)):
        if T[i][0] is not None: G[i + 1].append(T[i][0] + len(T) + 1)
        if T[i][1] is not None: G[i + 1].append(T[i][1] + len(T) + 1)
        if T[i][2] is not None: G[i + 1].append(T[i][2] + len(T) + 1)

    for i in range(len(T), len(G) - 1):
        G[i + 1].append(len(G) - 1)

    return G
def dfs_visit(G, GD, V, P, i):
    V[i] = True
    for nb in G[i]:
        idd = str(i) + "_" + str(nb)
        if not V[nb] and GD[idd] != 0:
            P[nb] = i
            dfs_visit(G, GD, V, P, nb)


def dfs(G, GD, s, t, P):
    V = [False for _ in range(len(G))]
    dfs_visit(G, GD, V, P, s)
    return V[t]


def fordFulkerson(G, s, t):
    GD = {}
    for u in range(len(G)):
        for v in range(len(G[u])):
            idd = str(u) + "_" + str(G[u][v])
            iddBack = str(G[u][v]) + "_" + str(u)
            GD[idd] = 1
            if GD.get(iddBack) == None:
                GD[iddBack] = 0

    for u in range(len(G)):
        for v in range(len(G[u])):
            idd = str(G[u][v]) + "_" + str(u)
            if GD[idd] == 0:
                G[G[u][v]].append(u)

    P = [None for _ in range(len(G))]
    max_flow = 0
    while dfs(G, GD, s, t, P):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, GD[str(P[current]) + "_" + str(current)])
            current = P[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = P[v]
            GD[str(u) + "_" + str(v)] -= current_flow
            GD[str(v) + "_" + str(u)] += current_flow
            v = P[v]
    return max_flow

runtests ( akademik )

