time = 0
visited = []


# def dfs(G):
#     global time, visited
#     visited = [False for _ in range(len(G))]
#     time = 0
#
#     for idx in range(len(G)):
#         if not visited[idx]:
#             dfsVisit(G, idx)
#
# def dfsVisit(G, s):
#     print(s)
#     global time, visited
#     time += 1
#     visited[s] = True
#
#     for el in G[s]:
#         if not visited[el]:
#             dfsVisit(G, el)
#     time += 1


def dfs(G):
    visited = [False for _ in range(len(G))]
    time = 0

    def dfsVisit(G, s):
        nonlocal time, visited
        print(s)
        time += 1
        visited[s] = True
        for el in G[s]:
            if not visited[el]:
                dfsVisit(G, el)
        time += 1

    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx)


G = [[1, 2],
     [0, 2],
     [0, 1]]

G = [[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]

dfs(G)
