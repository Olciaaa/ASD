# Adam Misztal

'''
Ważne!
Do stworzenia mojego programu wykorzystałem wiedze poznaną na wykładzie oraz w Cormenie

Opis algorytmu:
Jest to implementacja metody Forda-Fulkersona z użyciem zmodyfikowanego DFSa do wyszukiwania ścieżek powiększających
oraz superźródła do połączenia 2 wybranych miast. Działam na obiektach klas Edge i Vertex.

Opis działania:
Tworzę graf taki jak zostaje podany w funkcji maxflow, po czym dodaje do niego krawędzie w przeciwną stronę jeśli
takowej jeszcze nie ma. Dzięki temu możemy również cofać przepływ (krawędzie te mają pole isO ustawione na true
(isO = is opposite)). Następnie przypisuje krawędzie do wierzchołków. Potem wybieram 2 dowolne źródła (pętle przejdą
przez wszystkie możliwości) i dodaje krawędzie do superźródła które po sprawdzenia maksymalnego przepływu usuwam, aby
móc sprawdzić kolejne. Następnie puszczam DFSa na tym grafie dopóki można dotrzeć do źródła. DFS jest zmodufikowany
w taki sposób, że możemy iść po krawędzi tylko wtedy gdy:
1. należy do początkowego grafu, lub jest odwrotna do takowej
2. możliwy przepływ jest dodatni (cf>0)
W ten sposób znajduje ścieżki powiększające którymi na bieżąco uaktualniam wartości krawędzi w grafie.
Na koniec wybieram taką parę wierzchołków która da mi największy przepływ i zwracam wartość.

Złożoność:
- czasowa O(V*V*E*(f*))
- pamięciowa O(E)
V - liczba wierzchołków, E - liczba krawędzi, f* - wartość maksymalnego przepływu
'''

from zad9testy import runtests


class Edge:
    def __init__(self, from_v, to_v, value, index, isO):
        self.from_v = from_v  # z wierzchołka
        self.to_v = to_v  # do wierzchołka
        self.c = value  # wartość początkowa krawędzi
        self.cf = value  # aktualna dostępna przepustowość którą można wykorzystać
        self.f = 0  # ile paliwa płynie już po danej krawędzi
        self.opposite = None  # krawędź przeciwna
        self.index = index  # index dla wygody implementacyjnej
        self.isO = isO  # czy jest przeciwna do krawędzi należącej do grafu podanego, czy do niego należy

    def __str__(self):
        return f'Index: {self.index}, from: {self.from_v}, to: {self.to_v}, c: {self.c}, cf: {self.cf}, f: {self.f}'

    # zwraca skąd dokąd prowadzi krawędź
    def getVertices(self):
        return self.from_v, self.to_v


class Vertex:
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.visited = False

    def __str__(self):
        edges = []
        for edge in self.edges:
            edges.append(Edge.__str__(edge))
        return f'Index: {self.index}, edges: {edges}'


# f ukcja aktualizuje krawędzie o wartość nowej ścieżki powiększającej
def actualize_edges(max_flow, Taken):
    for edge in Taken:
        if not edge.isO:
            edge.cf -= max_flow
            edge.f += max_flow
            opposite_edge = edge.opposite
            if opposite_edge is not None and opposite_edge.isO:
                opposite_edge.cf = edge.f
        else:
            edge.cf -= max_flow
            opposite_edge = edge.opposite
            opposite_edge.cf += max_flow
            opposite_edge.f -= max_flow


# zmodyfikowany dfs
def DFS(ListOfVeritces, s, t):
    for vertex in ListOfVeritces:
        vertex.visited = False
    max_flow = float('inf')
    Taken = []

    def DFS_visit(ListOfVeritces, Taken, s, t):
        nonlocal max_flow
        tmp_max_flow = max_flow
        ListOfVeritces[s].visited = True
        for edge in ListOfVeritces[s].edges:
            if edge.to_v == t and edge.cf > 0:
                if edge.cf < max_flow:
                    max_flow = edge.cf
                Taken.append(edge)
                return True
            if not ListOfVeritces[edge.to_v].visited and edge.cf > 0:
                if edge.cf < max_flow:
                    max_flow = edge.cf
                if DFS_visit(ListOfVeritces, Taken, edge.to_v, t):
                    Taken.append(edge)
                    return True
                max_flow = tmp_max_flow
        return False

    if DFS_visit(ListOfVeritces, Taken, s, t):
        actualize_edges(max_flow, Taken)
        return max_flow
    else:
        return 0


# ta funkcja będzie służyła do zwracania maksmalnego indexu listy obiektów Vertex lub Edge (oba mają pole index)
def createIndex(List):
    return List[-1].index + 1


# funkcja dodająca do zadanego grafu kawędzie przeciwne jeśli ich nie ma
def create_opposites(ListOfEdges):
    for edge in ListOfEdges:
        if edge.opposite is None:
            found = False
            f, t = edge.getVertices()
            for second_edge in ListOfEdges:
                if second_edge.getVertices() == (t, f):
                    edge.opposite = second_edge
                    second_edge.opposite = edge
                    found = True
            if not found:
                second_edge = Edge(t, f, edge.c, createIndex(ListOfEdges), True)
                second_edge.cf = 0
                edge.opposite = second_edge
                second_edge.opposite = edge
                ListOfEdges.append(second_edge)


# funckja tworząca liste krawędzi i wierzchołków (obiekty klas Vertex i Edge)
def create_graph(G):
    ListOfEdges = [Edge(G[i][0], G[i][1], G[i][2], i, False) for i in range(len(G))]
    create_opposites(ListOfEdges)
    max_edge = max(G, key=lambda x: max(x[0], x[1]))
    max_v = max(max_edge[0], max_edge[1])
    ListOfVertices = [Vertex(i) for i in range(max_v + 1)]
    for edge in ListOfEdges:
        ListOfVertices[edge.from_v].edges.append(edge)
    return ListOfVertices, ListOfEdges


# tworzenie superźródła
def addSuperEnd(ListOfVertices, ListOfEdges, t1, t2, max_i):
    ListOfEdges.append(Edge(t1, max_i + 1, 10 ** 10, createIndex(ListOfEdges), False))
    ListOfEdges.append(Edge(t2, max_i + 1, 10 ** 10, createIndex(ListOfEdges), False))
    ListOfVertices[t1].edges.append(ListOfEdges[-2])
    ListOfVertices[t2].edges.append(ListOfEdges[-1])


# usunięcie superźródła i wyczyszczenie wartości krawędzi
def clearChanges(ListOfEdges, ListOfVertices, t1, t2):
    ListOfEdges.pop(-1)
    ListOfEdges.pop(-1)
    ListOfVertices[t2].edges.pop(-1)
    ListOfVertices[t1].edges.pop(-1)
    for edge in ListOfEdges:
        if not edge.isO:
            edge.cf = edge.c
            edge.f = 0
        else:
            edge.cf = 0


def findMaxFlow(ListOfVertices, ListOfEdges, s, t1, t2):
    max_i = ListOfVertices[-1].index
    addSuperEnd(ListOfVertices, ListOfEdges, t1, t2, max_i)
    out = 0
    x = DFS(ListOfVertices, s, max_i + 1)
    while x > 0:
        out += x
        x = DFS(ListOfVertices, s, max_i + 1)
    clearChanges(ListOfEdges, ListOfVertices, t1, t2)
    return out


def maxflow(G, s):
    ListOfVertices, ListOfEdges = create_graph(G)
    best = 0
    for i in range(len(ListOfVertices)):
        for j in range(i + 1, len(ListOfVertices)):
            if i != s and j != s:
                best = max(best, findMaxFlow(ListOfVertices, ListOfEdges, s, i, j))
    return best

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
