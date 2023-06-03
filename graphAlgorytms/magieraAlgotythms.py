from math import inf
from queue import *


def bsearch(S, l, r, key):
    while l <= r:
        m = (l + r) // 2
        if key == S[m]:
            return m
        elif key > S[m]:
            l = m + 1
        else:
            r = m - 1
    return -1


def bsearch_floor(S, l, r, key):  # O(log n)
    while l < r:
        m = (l + r + 1) // 2
        if key >= S[m]:
            l = m
        else:
            r = m - 1
    return l


def bsearch_roof(S, l, r, key):  # O(log n)
    while l < r:
        m = (l + r) // 2
        if key <= S[m]:
            r = m
        else:
            l = m + 1
    return r


def partition(T, p, r):  # O(n)
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[r], T[i + 1] = T[i + 1], T[r]
    return i + 1


def select(T, p, r, k):  # O(n)
    if p == r:
        return T[p]
    q = partition(T, p, r)
    if q == k:
        return T[q]
    elif k < q:
        return select(T, p, q - 1, k)
    else:
        return select(T, q + 1, r, k)


def quicksort(T, p, r):
    if p < r:
        q = partition(T, p, r)
        quicksort(T, p, q - 1)
        quicksort(T, q + 1, r)


def countsort(A, k):  # O(n)
    C = [0] * k
    B = [0] * len(A)

    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(len(A) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    for i in range(len(A)):
        A[i] = B[i]


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


# MAX HEAP - dla min heap na odwrót znaki porównania + decrease i increase key też
def heapify(A, n, i):  # O(log n)
    l = 2 * i + 1
    r = 2 * i + 2
    m = i
    if l < n and A[l] > A[m]:
        m = l
    if r < n and A[r] > A[m]:
        m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)


def buildheap(A):  # O(n)
    n = len(A)
    for i in range((n - 1 - 1) // 2, -1, -1):  # parent = (i - 1)//2
        heapify(A, n, i)


def heapsort(A):  # O(n log n)
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


def heap_pop(A):  # extract_max  O(log n)
    n = len(A)
    A[n - 1], A[0] = A[0], A[n - 1]
    res = A.pop()
    heapify(A, n, 0)
    return res


def increase_key(A, i,
                 new_val):  # zwykle zamiast i jest key -> i = map(key), używamy jakiegoś mapowania, żeby znaleźć indeks klucza
    A[i] = new_val
    while A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def decrease_key(A, i, new_val):
    A[i] = new_val
    heapify(A, len(A), i)  # heapify down


def add_to_heap(A, item):  # O(logn)  insert
    A.append(item)
    i = len(A) - 1
    while (i - 1) // 2 >= 0 and A[i] > A[(i - 1) // 2]:
        A[i], A[(i - 1) // 2] = A[(i - 1) // 2], A[i]
        i = (i - 1) // 2


def insertion_sort(head):  # head - wskaźnik na głowę listy bez wartownika
    new_head = Node()
    new_head.next = None
    new_head.val = -1

    tail = new_head
    while head is not None:  # O(n)
        prev = None
        temp = new_head
        while temp is not None and temp.val < head.val:  # znajdź miejsce, w które należy wstawić obecny element
            prev = temp
            temp = temp.next  # O(n^2)

        prev.next = head  # wstaw element do posortowanej listy i przesuń wskaźnik ze starej listy na kolejny element
        head = head.next
        prev.next.next = temp

    while tail.next is not None:  # przesuń ogon na koniec posortowanej listy
        tail = tail.next  # O(n)

    new_head.val = None
    return new_head, tail


# https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/ - DOBRZE ZAIMPLEMENTOWANE PQ JAKO HEAP


def lis(A):  # najdłuższy rosnący podciąg
    n = len(A)
    F = [-1] * n
    P = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
    index_max = max(range(len(F)), key=F.__getitem__)
    return max(F) + 2, index_max, P


def print_solution(A, P, i):
    if P[i] != -1:
        print_solution(A, P, P[i])
    print(A[i], " ", end="")


A = [13, 7, 21, 42, 8, 2, 44, 53]

length, i, P = lis(A)
print(length)
print_solution(A, P, i)
print("\n")


# problem knapsack
def knapsack(W, P, MaxW):  # W - masy, P - wartości
    n = len(W)
    F = [[0] * (MaxW + 1) for _ in range(n)]

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])
    return F[n - 1][MaxW], F


def getsolution(F, W, P, i, w):
    if i == 0:
        if w >= W[0]:
            return [0]
        return []
    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return getsolution(F, W, P, i - 1, w - W[i]) + [i]
    return getsolution(F, W, P, i - 1, w)


P = [60, 100, 120]
W = [10, 20, 30]
MaxW = 40
res, F = knapsack(W, P, MaxW)
print(res, getsolution(F, W, P, len(W) - 1, MaxW))
print()


# zadanie 1 - knapsack O(n * [sum P[i] from i = 0 to n - 1])
def knapsack2(W, P, MaxW):
    n = len(W)
    sum_ = sum(P)
    w = sum(W)
    F = [[0] + [w + 1] * sum_ for _ in range(n)]
    F[0][P[0]] = W[0]
    for i in range(1, n):
        for p in range(sum_ + 1):
            if p < P[i]:
                F[i][p] = F[i - 1][p]
            else:
                F[i][p] = min(F[i - 1][p], F[i - 1][p - P[i]] + W[i])
    for p in range(sum_, -1, -1):
        if F[n - 1][p] != w + 1 and F[n - 1][p] <= MaxW:
            return p, F
    return None, None


def getsolution2(F, W, P, i, p):
    if p == 0:
        return []
    if i == 0:
        return [0]
    if F[i - 1][p] == F[i][p]:
        return getsolution2(F, W, P, i - 1, p)
    return getsolution2(F, W, P, i - 1, p - P[i]) + [i]


P = [5, 2, 3, 7, 6, 13]
W = [7, 6, 10, 9, 42, 13]
n = len(W)
MaxW = 27
res, F = knapsack2(W, P, MaxW)
if res is not None:
    print(res, getsolution2(F, W, P, n - 1, res))
else:
    print("Brak rozwiązania")
print()


# zadanie 2 - suma podzbioru/podciągu - założenie, że można wziąc pusty podciąg/podzbiór
def sum_of_substring(A, T):  # wersja dla liczb naturalnych - złożoność pseuodwielomianowa O(n*T)
    n = len(A)
    F = [[False] * (T + 1) for _ in range(n)]
    F[0][0] = True
    if A[0] <= T:
        F[0][A[0]] = True
    for i in range(1, n):
        x = A[i]
        for j in range(0, T + 1):
            if j < x:
                F[i][j] = F[i - 1][j]
            else:
                F[i][j] = F[i - 1][j] or F[i - 1][j - x]
        if F[i][T]:
            return True, F, i
    return False, F, None


def get_substring(A, T, F, k):
    if T == 0:
        return []
    if k == 0:
        return [A[0]]
    if F[k - 1][T]:
        return get_substring(A, T, F, k - 1)
    return get_substring(A, T - A[k], F, k - 1) + [A[k]]


A = [2, 6, 3, 72, 10, 11]
T = 14
res, F, k = sum_of_substring(A, T)
if res:
    print(T, get_substring(A, T, F, k))
else:
    print("Brak rozwiązania")


def bridges(G):
    def DFS_visit(G, v):
        nonlocal time, visited, parent, d, low, bridge_tab
        visited[v] = True
        d[v] = time
        low[v] = time
        time += 1

        for i in G[v]:
            if not visited[i]:
                parent[i] = v
                DFS_visit(G, i)
                low[v] = min(low[v], low[i])  # dziecko w drzewie DFS

                if low[i] == d[i]:  # most - alternatywnie low[i] > d[v]
                    # dla punktów artykulacji - low[i] >= d[v] -> v to punkt artykulacji
                    bridge_tab.append((v, i))

            elif parent[v] != i:  # krawędź wsteczna
                low[v] = min(low[v], d[i])

    time = 0
    visited = [False] * len(G)
    parent = [-1] * len(G)
    d = [inf] * len(G)
    low = [inf] * len(G)
    bridge_tab = []

    for v in range(len(G)):
        if not visited[v]:
            DFS_visit(G, v)

    return bridge_tab


G = [
    [1, 2, 3],
    [0, 2],
    [0, 1],
    [0, 4],
    [3]
]

print(bridges(G))


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


print(is_bipartite(G))


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


G = [
    [2, 3],
    [0],
    [1],
    [4],
    []
]

print(strongly_connected_components(G))


def topological_sort(G):
    def DFS_visit(G, v):
        nonlocal visited, stack
        visited[v] = True

        for i in G[v]:
            if not visited[i]:
                DFS_visit(G, i)
        stack.append(v)

    visited = [False] * len(G)
    stack = []

    for v in range(len(G)):
        if not visited[v]:
            DFS_visit(G, v)

    stack.reverse()
    return stack


G = [
    [1, 2],
    [],
    [1, 3],
    [4, 5, 6],
    [],
    [],
    []
]

print(topological_sort(G))


def Djikstra(G, s):  # dla list sąsiedztwa G[v]: pary [u, w(v, u)] ->  O(V+E)
    PQ = PriorityQueue()

    visited = [False] * len(G)
    parent = [None] * len(G)
    d = [inf] * len(G)
    d[s] = 0

    PQ.put((0, s))
    while not PQ.empty():
        _, v = PQ.get()
        if not visited[v]:
            for u, w in G[v]:
                if not visited[u]:
                    if d[u] > d[v] + w:
                        d[u] = d[v] + w
                        parent[u] = v
                        PQ.put((d[u], u))
            visited[v] = True
    return d, parent


G = [
    [(1, 4), (7, 8)],
    [(0, 4), (2, 8), (7, 11)],
    [(1, 8), (3, 7), (5, 4), (8, 2)],
    [(2, 7), (4, 9), (5, 14)],
    [(3, 9), (5, 10)],
    [(2, 4), (3, 14), (4, 10), (6, 2)],
    [(5, 2), (7, 1), (8, 6)],
    [(0, 8), (1, 11), (6, 1), (8, 7)],
    [(2, 2), (6, 6), (7, 7)],
]

print("DJIKSTRA", Djikstra(G, 0))


def Djikstra2(G, s):  # dla reprezentacji macierzowej G[v][u] = w(v, u) -> O(V**2)

    def min_index(n):
        nonlocal visited, d
        min_ = inf
        index = -1
        for i in range(n):
            if not visited[i] and d[i] < min_:
                index = i
                min_ = d[i]
        return index

    n = len(G)
    visited = [False] * n
    parent = [None] * n
    d = [inf] * n
    d[s] = 0

    for _ in range(n):  # bo bierzemy n wierzchołków w sumie
        u = min_index(n)
        for v in range(n):
            if not visited[v]:
                if G[u][v] > 0 and d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]
                    parent[v] = u
        visited[u] = True
    return d, parent


G = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

print(Djikstra2(G, 0))


# Kruskal O(E log E)
class Node:
    def __init__(self):  # make_set
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def Kruskal_MST(G, V):  # dla listy krawędzi postaci [v1, v2, value], V - liczba wierzchołków O(ElogE)
    A = []
    vertices = [Node() for _ in range(V)]
    G.sort(key=lambda x: x[2])

    count = 0
    i = 0

    while count < V - 1:
        x = find(vertices[G[i][0]])
        y = find(vertices[G[i][1]])

        if x != y:
            count += 1
            A.append(G[i])
            union(x, y)

        i += 1
    return A


G = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

print(Kruskal_MST(G, 4))


# Bellmana - Forda O(V * E)
def BellmanFord(G, V, s):  # graf reprezentowany listą krawędzi, V to liczba wierzchołków w grafie
    parent = [None] * V
    d = [inf] * V
    d[s] = 0
    for _ in range(V - 1):
        for edge in G:
            u, v, w = edge
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                parent[v] = u

    check = False  # czy istnieją ujemne cykle
    for edge in G:
        u, v, w = edge
        if d[v] > d[u] + w:
            check = True
            break

    return check, d, parent


G = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
print(BellmanFord(G, 5, 0))


# Prima - O(E log V)
def Prim_MST(
        G):  # dla reprezentacji macierzowej G[v][u] - wartość krawędzi z v do u O(V**2), dla list sąsiedztwa postaci G[v] = [..., (u, value(v, u)), ...] O(ElogV)
    PQ = PriorityQueue()

    visited = [False] * len(G)
    parent = [None] * len(G)
    weight = [inf] * len(G)
    weight[0] = 0

    PQ.put((weight[0], 0))
    while not PQ.empty():
        _, v = PQ.get()
        if not visited[v]:
            for i in range(len(G[v])):
                u, w = G[v][i]
                if not visited[u] and w < weight[u]:
                    parent[u] = v
                    weight[u] = w
                    PQ.put((weight[u], u))
            visited[v] = True
    return parent


G = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8), (4, 9)],
    [(1, 5), (2, 7), (3, 9)]
]

parent = Prim_MST(G)
for i in range(1, len(G)):
    print(parent[i], i)


def transitive_closure(G):
    T = [[0 for _ in range(len(G))] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if i == j or G[i][j] != 0:
                T[i][j] = 1

    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                T[i][j] = T[i][j] or (T[i][k] and T[k][j])

    return T


def Floyd_Warshall(G):
    n = len(G)
    T = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                T[i][j] = G[i][j]
            if i == j:
                T[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = min(T[i][j], T[i][k] + T[k][j])

    return T


# ---------------------------------------------------------------- #
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None


def insert(root, key, prev=None):
    if root is None:
        new = BSTNode(key)
        new.parent = prev
        return new

    if key < root.key:
        root.left = insert(root.left, key, root)
    else:
        root.right = insert(root.right, key, root)

    return root


def insert_iter(root, key):
    new_node = BSTNode(key)
    if root is None:
        return new_node

    prev = None
    while root is not None:
        prev = root
        if key < root.key:
            root = root.left
        else:
            root = root.right

    new_node.parent = prev
    if key < prev.key:
        prev.left = new_node
    else:
        prev.right = new_node

    return


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def min_(root):
    while root.left is not None:
        root = root.left
    return root


def max_(root):
    while root.right is not None:
        root = root.right
    return root


def pre_and_suc(root, key, pre=None, suc=None):  # zwraca w kolejnośc prev, next
    if root is None:
        return pre, suc

    if root.key == key:
        if root.left is not None:
            temp = root.left
            while temp.right:
                temp = temp.right
            pre = temp

        if root.right is not None:
            temp = root.right
            while temp.left:
                temp = temp.left
            suc = temp

        return pre, suc

    if key < root.key:
        suc = root
        return pre_and_suc(root.left, key, pre, suc)
    else:
        pre = root
        return pre_and_suc(root.right, key, pre, suc)


def previous(root, key):
    return


def succcesor(root, key):
    return


def inorder(root):  # O(n)
    if root is None:
        return
    inorder(root.left)
    print(root.key)
    inorder(root.right)


R = insert_iter(None, 20)
insert_iter(R, 10)
insert_iter(R, 27)
insert_iter(R, 22)
insert_iter(R, 30)
insert_iter(R, 28)
insert_iter(R, 35)
insert_iter(R, 40)
insert_iter(R, 5)
insert_iter(R, 15)
insert_iter(R, 13)

res = pre_and_suc(R, 28)
print(res[0].key, res[1].key)

print()

inorder(R)