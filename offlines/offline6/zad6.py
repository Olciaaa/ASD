from zad6testy import runtests
from queue import Queue

def bfs(G, s, t):
    visited = [False for _ in range(len(G))]
    distanceFromS = [-1 for _ in range(len(G))]
    q = Queue()
    q.put(s)
    visited[s] = True
    distanceFromS[s] = 0

    while not q.empty():
        s = q.get()
        if s == t: return distanceFromS

        for i in range(len(G[s])):
            if not visited[G[s][i]]:
                q.put(G[s][i])
                visited[G[s][i]] = True
                distanceFromS[G[s][i]] = distanceFromS[s] + 1
    return distanceFromS

def longer( G, s, t ):
    frontToBack = bfs(G, s, t)
    backToFront = bfs(G, t, s)

    print(frontToBack)
    print(backToFront)

    i = t
    while i > 0:
        curr_el = i
        i = curr_el - 1
        curr_val = backToFront[i]
        count = 0
        curr_minimum = frontToBack[i]

        while backToFront[i] == curr_val:
            if frontToBack[i] == curr_minimum:
                count += 1
            else:
                count = 1
                curr_minimum = frontToBack[i]
            i -= 1
        i += 1

        if count < 2: return (i, curr_el)
        i -= 1

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True)