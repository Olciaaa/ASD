from collections import deque
from zad1testy import runtests

def BFS(G, V, s, t):
    Q = deque()
    Q.append(s)

    while Q:
        v = Q.popleft()
        V[v] = True

        for nb in G[v]:
            if not V[nb]:
                Q.append(nb)


def intuse(I, x, y):
    DICT = {}
    DICT2 = {}

    current = 0
    for i in range(len(I)):
        if DICT.get(I[i][0]) == None:
            DICT[I[i][0]] = current
            DICT2[current] = I[i][0]
            I[i] = (current, I[i][1])
            current += 1
        else:
            I[i] = (DICT[I[i][0]], I[i][1])

        if DICT.get(I[i][1]) == None:
            DICT[I[i][1]] = current
            DICT2[current] = I[i][1]
            I[i] = (I[i][0], current)
            current += 1
        else:
            I[i] = (I[i][0], DICT[I[i][1]])

    n = current + 1

    G = [[] for _ in range(n)]
    G2 = [[] for _ in range(n)]
    for e in I:
        if DICT2[e[0]] < DICT2[e[1]]:
            G[e[0]].append(e[1])
            G2[e[1]].append(e[0])
        else:
            G[e[1]].append(e[0])
            G2[e[0]].append(e[1])

    Vs = [False for _ in range(n)]
    Vt = [False for _ in range(n)]

    BFS(G, Vs, DICT[x], DICT[y])
    BFS(G2, Vt, DICT[y], DICT[x])

    res = []
    for i in range(len(I)):
        el = I[i]
        if DICT2[el[0]] < DICT2[el[1]]:
            if Vs[el[0]] and Vt[el[1]]:
                res.append(i)
        else:
            if Vs[el[1]] and Vt[el[0]]:
                res.append(i)

    return res


runtests( intuse )