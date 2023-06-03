from zad9testy import runtests
from queue import Queue
capacities = []
n = 0

def maxflow( G,s ):
    global capacities, n

    for el in G:
        if max(el[1], el[0]) > n: n = max(el[1], el[0])

    capacities = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for el in G:
        capacities[el[0]][el[1]] = el[2]

    return 0

def minConnection(s, t):
    visited = [False for _ in range(n + 1)]
    q = Queue()
    q.put(s)
    visited[s] = True
    paths = [[] for _ in range(n + 1)]

    while not q.empty():
        s = q.get()
        if s == t: return paths[]

        for v in range(n + 1):
            if

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( maxflow, all_tests = False )