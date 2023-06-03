# The Ford-Fulkerson algorithm is a greedy algorithm that computes the maximum flow in a flow network (G).
from math import inf


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