from egzP5btesty import runtests 

def koleje ( B ):
    for i in range(len(B)):
        B[i] = (min(B[i][0], B[i][1]), max(B[i][0], B[i][1]))

    B = set(B)

    n = 0
    for el in B:
        n = max(el[0], el[1], n)

    tab = [[] for _ in range(n + 1)]

    for el in B:
        tab[el[0]].append(el[1])
        tab[el[1]].append(el[0])

    #print(tab)
    #articulation(tab)
    return articulation(tab)

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
runtests ( koleje, all_tests=True )