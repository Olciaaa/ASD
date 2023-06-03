A = []
class Node:
    def __init__(self, val):
        self.rank = 0
        self.parent = self
        self.val = val

#przepinanko do głowy zbioru i fajnie, zamortyzowana O(1)
def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

#łączenie zbiorów, zamortyzowana O(1)
def union(x, y, price):
    global A
    x = find(x)
    y = find(y)
    if x == y:
        return

    A.append((x.val, y.val, price))
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def Kruskal_MST(G, V):  # dla listy krawędzi postaci [v1, v2, value], V - liczba wierzchołków O(ElogE)
    global A
    vertices = [Node(i) for i in range(V)]
    G.sort(key=lambda x: x[2])

    for el in G:
        union(vertices[el[0]], vertices[el[1]], el[2])

    return A


G = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

print(Kruskal_MST(G, 4))
