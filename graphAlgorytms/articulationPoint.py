time = 0


def dfs(G, ART, LOW, D, P, v):
    global time
    children = 0

    time += 1
    LOW[v] = time
    D[v] = time

    for s in G[v]:
        if D[s] is None:
            children += 1
            dfs(G, ART, LOW, D, P, s)

            if LOW[s] >= D[v]:
                ART[v] = True
            LOW[v] = min(LOW[v], LOW[s])
        else:
            LOW[v] = min(LOW[v], D[s])

    return children


def articulation(G):
    # Czas odwiedzenia
    global time

    n = len(G)
    # Tablica pamietajaca czy wierzchołek jest punktem artykulacji
    ART = [False for _ in range(n)]
    # LOW z wykładu
    LOW = [None for _ in range(n)]
    # Czas odwiedzenia, (D)iscovery time
    D = [None for _ in range(n)]
    # Tablica parentów
    P = [None for _ in range(n)]

    for i in range(n):
        if D[i] is None:
            if dfs(G, ART, LOW, D, P, i) > 1:
                ART[i] = True
            else:
                ART[i] = False

    points = 0
    for i in range(n):
        if ART[i] == True:
            points += 1
    return points

'''time = 0
articulationPoints = []
low = []
visitedTime = []
isProceed = []
parent = []
# low = min{visitedTime(v), d(krawędź_wsteczna_v), low(dziecko_v)}

def dfs(G):
    global time, visitedTime, low, parent, isProceed
    visitedTime = [-1 for _ in range(len(G))]
    low = [-1 for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    isProceed = [False for _ in range(len(G))]
    time = 0

    for idx in range(len(G)):
        if visitedTime[idx] == -1:
            if len(G[idx]) >= 2:
                articulationPoints.append(idx)
            dfsVisit(G, idx)
    for i in range(len(G)):
        for child in G[i]:
            if low[child] >= visitedTime[i] and i not in articulationPoints and parent[i] != child:
                articulationPoints.append(i)
    # print(low)
    # print(visitedTime)
    print(articulationPoints)
    # print(parent)


def dfsVisit(G, s):
    # print(s)
    global time, visitedTime, low, isProceed, parent
    time += 1
    visitedTime[s] = time
    low[s] = time

    for el in G[s]:
        if visitedTime[el] == -1:
            parent[el] = s
            dfsVisit(G, el)
            low[s] = min(low[s], low[el])
        elif parent[s] != el and not isProceed[el]:
            low[s] = min(low[s], visitedTime[el])
    isProceed[s] = True


G = [[1, 2, 3, 5], [0, 4, 5], [0, 3], [0, 2, 6, 7], [1, 5], [0, 1, 4], [3, 7], [3, 6]]
# G = [[1,2,3],[0,2],[0,1],[0,4,5],[3,5],[3,4]]
# G = [[1, 2, 3], [0, 2, 14], [0, 1], [0], [11, 12], [6, 9], [5, 7, 8], [6], [8], [5], [15], [4, 15], [4, 15], [14, 16],
#    [1, 13, 16], [10, 11, 12], [13, 14]]
dfs(G)'''
