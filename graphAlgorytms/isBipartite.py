from queue import Queue

def is_bipartite(G):
    def BFS(G, s):
        nonlocal color

        Q = Queue()
        color[s] = 1
        Q.put(s)
        while not Q.empty():
            v = Q.get()
            for i in G[v]:
                if color[v] == color[i]:  # jeśli wierzchołki mają ten sam kolor to graf nie jest dwudzielny
                    return False
                if color[i] == -1:  # jeśli nie odwiedzono wierzchołka, przypisz mu kolor i dodaj do kolejki
                    color[i] = int(not color[v])
                    Q.put(i)
        return True

    color = [-1] * len(G)  # -1 - nie przypisano koloru, 0 - kolor 1, 1 - kolor 2

    for v in range(len(G)):
        if color[v] == -1:  # jeśli do wierzchołka nie przypisano koloru, to zbadaj spójną składową do niego należącą
            if not BFS(G, v):
                return False
    return True