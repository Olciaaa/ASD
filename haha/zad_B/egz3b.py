from asyncio import PriorityQueue
from egz3btesty import runtests
from math import inf

def convert_to_lista_sasiedztwa(L):
    n = len(L[0])

    graf = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        wers = L[i]
        for j in range(n):
            if wers[j] == ".":
                graf[i][j] = 1

    L = [[n ** 2, n ** 2, n ** 2] for _ in range(n ** 2 + 1)]
    L[n ** 2] = []

    for i in range(n):
        for j in range(n):
            if graf[i][j] == 1:
                up, down, right = n ** 2, n ** 2, n ** 2
                if i > 0:
                    up = (i - 1) * n + j
                if i != n - 1:
                    down = (i + 1) * n + j
                if j != n - 1:
                    right = i * n + j + 1
                L[i * n + j] = up, right, down

    return L



# def Bellman_Ford(L,s):
#     n = len(G)
#     parent = [None for _ in range(n)]
#     d = [inf for i in range(n)]
#     d[s] = 0
#     w = -1
#     for _ in range(n-1):
#         for edge in L:
#             u,v = edge
#             if d[u] + w < d[v] and:
#                 d[v] = d[u] + w
#                 parent[v] = u
#
def djikstra(L, s):
    PQ = PriorityQueue()
    n = len(L)
    long = [inf for _ in range(n)]
    waga = 0
    PQ.put((waga, s, -1))

    while not PQ.empty():
        waga, u, last = PQ.get()
        waga *= -1

        for v in L[u]:
            if long[v] >= waga - 1 and v != last and v != n-1:
                long[v] = waga - 1
                PQ.put(((waga - 1)*(-1), v, u))

    return long[-2]


def maze(L):
    #tutaj jest dodany warunek
    if L[0][0] == "#" or L[len(L)-1][len(L)-1] == "#":
        return -1
    #

    L = convert_to_lista_sasiedztwa(L)
    wynik = djikstra(L,0)

    #I tutaj również
    if wynik == inf:
        return -1
    #

    return -wynik


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=False)