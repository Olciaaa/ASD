time = 0
visited = []
processedTimeQueue = []

def dfs(G):
    global time, visited, processedTimeQueue
    components = []
    visited = [False for _ in range(len(G))]
    time = 0

    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx)

    visited = [False for _ in range(len(G))]
    changedG = changeConnectionDest(G)
    processedTimeQueue = processedTimeQueue[::-1]
    for el in processedTimeQueue:
        if not visited[el]:
            tab = []
            dfsVisitC(changedG, el, tab)
            components.append(tab)
    return components


def changeConnectionDest(G):
    newG = [[] for _ in range(len(G))]
    for idx in range(len(G)):
        for el in G[idx]:
            newG[el].append(idx)
    return newG


def dfsVisitC(changedG, s, tab):

    global time, visited, processedTimeQueue
    visited[s] = True

    for el in changedG[s]:
        if not visited[el]:
            dfsVisitC(changedG, el, tab)

    tab.append(s)


def dfsVisit(G, s):
    global time, visited, processedTimeQueue
    time += 1
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            dfsVisit(G, el)

    processedTimeQueue.append(s)
    time += 1


G = [[1, 4, 5], [2, 4, 5, 8, 11], [6], [1, 7], [8], [2, 8], [5, 7, 9], [], [4], [5, 7], [8, 11], [8, 9, 12], [3, 6, 9]]
print(dfs(G))

#Magiera version
def strongly_connected_components(G):
    def DFS_visit1(G, v):
        nonlocal visited, stack
        visited[v] = True

        for i in G[v]:
            if not visited[i]:
                DFS_visit1(G, i)
        stack.append(v)

    def DFS_visit2(G_reversed, v, flag):
        nonlocal visited, SCC
        visited[v] = True

        for i in G_reversed[v]:
            if not visited[i]:
                SCC[flag].append(i)
                DFS_visit2(G_reversed, i, flag)

    stack = []
    visited = [False] * len(G)

    for v in range(len(G)):
        if not visited[v]:
            DFS_visit1(G, v)

    G_reversed = [[] for _ in range(len(G))]
    for u in range(len(G)):
        for v in G[u]:
            G_reversed[v].append(u)

    for i in range(len(visited)):
        visited[i] = False

    flag = 0
    SCC = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            SCC.append([v])
            DFS_visit2(G_reversed, v, flag)
            flag += 1

    return SCC

G = [[1, 4, 5], [2, 4, 5, 8, 11], [6], [1, 7], [8], [2, 8], [5, 7, 9], [], [4], [5, 7], [8, 11], [8, 9, 12], [3, 6, 9]]
print(strongly_connected_components(G))