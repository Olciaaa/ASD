from queue import Queue

def bfs(G, s):
    q = Queue()
    visited = [False for _ in range(len(G))]

    visited[s] = True
    q.put(G[s])

    while not q.empty():
        u = q.get()
        print(u)

        for el in u:
            if visited[el] == False:
                visited[el] = True
                q.put(G[el])

G = [ [1, 2],
[0, 2],
[0, 1] ]
G = [[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]

bfs(G, 0)