'''
Dany jest ciąg przedziałów postaci [ai, bi]. Dwa przedziały można skleić, jeśli mają dokładnie jeden punkt wspólny.
Podaj algorytm, który sprawdza, czy da się uzyskać przedział [a, b] poprzez sklejanie odcinków.
'''
from queue import Queue


def isPossibleToConn(G, s, e):
    G = makeGraph(G)
    return bfs(G, s, e)

def bfs(G, s, e):
    visited = [False for _ in range(len(G))]
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        s = q.get()

        if s == e: return True

        for i in range(len(G[s])):
            if not visited[G[s][i]]:
                q.put(G[s][i])
                visited[G[s][i]] = True

    return False

def makeGraph(G):
    maximum = 0
    for el in G:
        maximum = max(maximum, el[0], el[1])

    tab = [[] for _ in range(maximum + 1)]

    for el in G:
        tab[el[0]].append(el[1])
        tab[el[1]].append(el[0])

    return tab

T = [(1, 2), (1, 13), (12, 15), (1, 12), (2, 6), (6, 12), (3, 4), (2, 3), (3, 5), (1, 4)]
a = 1
b = 13
print(isPossibleToConn(T, a, b))

T = [(1, 2), (1, 15), (12, 15), (1, 12), (2, 6), (6, 17), (3, 4), (2, 3), (3, 5), (1, 4)]
a = 1
b = 13
print(isPossibleToConn(T, a, b))