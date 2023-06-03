last_visited = []
cycle = []

class Flag:
    def __init__(self):
        self.exists = True

def findCycle(G):
    global last_visited
    last_visited = [0 for _ in range(len(G))]
    G2 = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for nb in G[i]:
            if i < nb:
                flag = Flag()
                G2[i].append((nb, flag))
                G2[nb].append((i, flag))

    dfsVisit(G2, 0)

def dfsVisit(G, s):
    global last_visited, cycle

    for i in range(last_visited[s], len(G[s])):
        el = G[s][i]
        if el[1].exists:
            el[1].exists = False
            last_visited[s] = i + 1
            dfsVisit(G, el[0])
    cycle.append(s)

def isEuler(G):
    for el in G:
        if len(el) % 2 == 1:
            return False
    #i jeszcze sprawdzamy bfs albo dfs czy każdy może być odwiedzony (soł spójność)
    return True

G = [(4, 5), (2, 3, 4, 5), (1, 3, 4, 5), (1, 2), (0, 1, 2, 5), (0, 1, 2, 4)]

G = [
    [1, 2],
    [0, 2, 3, 4],
    [0, 1, 3, 4],
    [1, 5, 4, 2],
    [2, 3, 5, 1],
    [3, 4]
]
if isEuler(G):
    findCycle(G)
    print(cycle)
else:
    print("nie ma")

#[0, 1, 2, 3, 1, 4, 3, 5, 4, 2, 0]
