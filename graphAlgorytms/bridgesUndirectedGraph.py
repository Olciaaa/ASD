time = 0
visited = []
visitedTime = []
low = []
isProcessed = []
parent = []


def bridges(G):
    global visitedTime, low, parent
    dfs(G)
    print(visitedTime)
    print(low)

    for i in range(len(G)):
        if visitedTime[i] == low[i] and parent[i] != -1:
            print(parent[i], " - ", i)


def dfs(G):
    global time, visited, low, visitedTime, isProcessed, parent
    low = [0 for _ in range(len(G))]
    visitedTime = [0 for _ in range(len(G))]
    isProcessed = [False for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    time = 0

    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx)


def dfsVisit(G, s):
    global time, visited, visitedTime, isProcessed, low, parent
    time += 1
    visitedTime[s] = time
    low[s] = time
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            parent[el] = s
            dfsVisit(G, el)
            low[s] = min(low[s], low[el])
        elif parent[s] != el:
            if not isProcessed[el]:
                low[s] = min(low[s], visitedTime[el])

    isProcessed[s] = True


G = [[1, 2, 3], [0, 2, 14], [0, 1], [0], [11, 12], [6, 9], [5, 7, 8], [6], [8], [5], [15], [4, 15], [4, 15], [14, 16],
     [1, 13, 16], [10, 11, 12], [13, 14]]
# G = [[1, 6], [0, 2], [1, 3, 6], [2, 4, 5], [3, 5], [3, 4], [0, 2, 7], [6]]
bridges(G)
