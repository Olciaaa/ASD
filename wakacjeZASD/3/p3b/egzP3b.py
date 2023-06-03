from egzP3btesty import runtests
from queue import PriorityQueue

A = set()
value = 0


class Node:
    def __init__(self, val):
        self.rank = 0
        self.parent = self
        self.val = val


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y, price):
    global A, value
    x = find(x)
    y = find(y)
    if x == y:
        A.add((x.val, y.val, price))
        return

    value += abs(price)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def mst(G, n):
    vertices = [Node(i) for i in range(n)]
    G.sort(key=lambda x: x[2])

    for el in G:
        union(vertices[el[0]], vertices[el[1]], el[2])


def countValues(G):
    val = 0

    for el in G:
        val += abs(el[2])
    return val


def lufthansa(G):
    global value, A
    value = 0
    A = set()
    graph = []
    for i in range(len(G)):
        for ell in G[i]:
            if i < ell[0]:
                graph.append((i, ell[0], -ell[1]))

    # print(G)
    # print(graph)
    mst(graph, len(G))
    # print(value)
    # print(A)
    # tutaj proszę wpisać własną implementację
    maximum = 0
    A = list(A)
    for el in A:
        maximum = max(maximum, abs(el[2]))

    return countValues(graph) - value - maximum


runtests(lufthansa, all_tests=True)
G = [
    [(1, 15), (2, 5), (3, 10)],
    [(0, 15), (2, 8), (4, 5), (5, 12)],
    [(0, 5), (1, 8), (3, 5), (4, 6)],
    [(0, 10), (2, 5), (4, 2), (5, 11)],
    [(1, 5), (2, 6), (3, 2), (5, 2)],
    [(1, 12), (4, 2), (3, 11)]
]
# lufthansa(G)
