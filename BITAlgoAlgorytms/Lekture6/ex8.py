'''
Średnicą drzewa nazywamy odległość między jego najbardziej oddalonymi od siebie wierzchołkami. Napisz algorytm, który
przyjmując na wejściu drzewo (niekoniecznie binarne!) w postaci listy krawędzi zwróci jego średnicę.
'''
from queue import Queue

def diameter(G):
    v = 0

    for i in range(len(G)):
        if len(G[i]) == 1:
            v = i
            break
    values = bfs(G, v)

    max_idx = 0
    max_val = values[0]
    for i in range(len(values)):
        if values[i] > max_val:
            max_idx = i
            max_val = values[i]

    values = bfs(G, max_idx)
    return max(values)

def bfs(G, s):
    visited = [False for _ in range(len(G))]
    distanceFromS = [0 for _ in range(len(G))]
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        s = q.get()

        for i in range(len(G[s])):
            if not visited[G[s][i]]:
                q.put(G[s][i])
                visited[G[s][i]] = True
                distanceFromS[G[s][i]] = distanceFromS[s] + 1

    return distanceFromS

G5 = [[2], [2], [0, 1, 3], [2, 4], [3, 5, 8], [4, 6, 7], [5], [5], [4, 9], [8]]
G5 = [[1],[0,2],[1,5,3],[2,4],[3], [2]]
print(diameter(G5))