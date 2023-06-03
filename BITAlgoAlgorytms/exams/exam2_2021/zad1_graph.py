from queue import Queue

from zad1testy import runtests

def intuse( I, x, y ):
    G, dict = makeGraph(I)

    x = dict.get(x)
    y = dict.get(y)
    if x is None or y is None:
        return []

    visFromX= bfs(G, x, y, len(I))
    visFromY = bfs(G, y, x, len(I))

    if visFromY is None or visFromY is None:
        return []

    keyss = dict.keys()
    keys = []
    for key in keyss:
        keys.append(key)
    results = []
    conns = [False for i in range(len(dict))]
    for i in range(len(G)):
        if visFromX[i] and visFromY[i]:
            conns[i] = True

    for i in range(len(I)):
        if dict[I[i][0]] < dict[I[i][1]]:
            if conns[dict[I[i][0]]] and conns[dict[I[i][1]]]:
                results.append(i)
        else:
            if conns[dict[I[i][1]]] and conns[dict[I[i][0]]]:
                results.append(i)

    return results

def bfs(G, s, e, n):
    visited = [False for _ in range(len(G))]
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        v = q.get()
        if v == e:
            return visited
        for u, idx in G[v]:
            if not visited[u]:
                q.put(u)
                visited[u] = True
    return None


def makeGraph(Data):
    idx = 0
    dict = {}
    for el in Data:
        if dict.get(el[0]) == None:
            dict.update({el[0]: idx})
            idx += 1
        if dict.get(el[1]) == None:
            dict.update({el[1]: idx})
            idx += 1
    G = [[] for _ in range(len(dict))]
    idx = 0
    for el in Data:
        v1 = dict[el[0]]
        v2 = dict[el[1]]

        G[v1].append((v2, idx))
        G[v2].append((v1, idx))
        idx += 1
    return G, dict
runtests( intuse )