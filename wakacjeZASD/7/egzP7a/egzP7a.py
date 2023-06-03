from math import inf
from queue import PriorityQueue

from egzP7atesty import runtests

def akademik( T ):
    print(T)
    return rec(T, [], 0, [])

def rec(T, dynamic, idx, used):
    if idx == len(T):
        return 0

    minimum = inf

    if T[idx][0] is not None and T[idx][0] not in used:
        minimum = min(minimum, rec(T, dynamic, idx + 1, used + [T[idx][0]]))

    if T[idx][1] is not None and T[idx][1] not in used:
        minimum = min(minimum, rec(T, dynamic, idx + 1, used + [T[idx][1]]))

    if T[idx][2] is not None and T[idx][2] not in used:
        minimum = min(minimum, rec(T, dynamic, idx + 1, used + [T[idx][2]]))

    if T[idx][0] == T[idx][1] == T[idx][2] and T[idx][0] is None:
        return rec(T, dynamic, idx + 1, used)
    return min(minimum, rec(T, dynamic, idx + 1, used) + 1)
runtests ( akademik )
'''
def prim_algorithm(graph, source):
    queue = PriorityQueue()
    parent = [None] * len(graph)
    key = [inf] * len(graph)
    key[source] = 0
    visited = [False] * len(graph)
    visited[source] = True
    queue.put((0, source))
    while not queue.empty():
        dist, u = queue.get()
        visited[u] = True
        for i in range(len(graph)):
            if key[i] > graph[u][i] and not visited[i]:
                parent[i] = u
                key[i] = graph[u][i]
                queue.put((key[i], i))
    result = []
    for i in range(len(parent)):
        if parent[i] is not None:
            result.append((i, parent[i], key[i]))
    return result


def buildGraph(T):
    size = 0

    for el in T:
        if el[0] is not None:
            size = max(size, el[0])
        if el[1] is not None:
            size = max(size, el[1])
        if el[2] is not None:
            size = max(size, el[2])

    size += 1

    G = [[1 for _ in range(size + 1)]for _ in range(size + 1)]

    for el in T[0]:
        if el is not None:
            G[0][el + 1] = 0

    for i in range(1, len(T)):
        prev = T[i - 1]
        curr = T[i]

        for elP in prev:
            for elC in curr:
                if elP is not None and elC is not None:
                    G[elP + 1][elC + 1] = 0

    return G'''
