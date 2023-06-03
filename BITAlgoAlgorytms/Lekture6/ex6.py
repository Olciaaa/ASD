'''
Dostajemy na wejściu listę krawędzi drzewa (niekoniecznie binarnego!) oraz wyróżniony wierzchołek - korzeń. Każdy
wierzchołek tworzy swoje własne poddrzewo. Dla każdego wierzchołka, wyznacz ilość wierzchołków w jego poddrzewie.
'''
visited = []
children = []

def findChildren(G):
    global visited, children

    children = [0 for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    dfs(G, 3)
    print(children)

def dfs(G, v):
    global visited, children

    visited[v] = True
    haha = 0
    for u in G[v]:
        if not visited[u]:
            haha += dfs(G, u)

    children[v] = haha
    return haha + 1

G5 = [[2], [2], [0, 1, 3], [2, 4], [3, 5, 8], [4, 6, 7], [5], [5], [4, 9], [8]]
findChildren(G5)
