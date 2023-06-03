
'''Pewien podróżnik chce przebyć trasę z punktu A
do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści
się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to
łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym
wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z
punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.'''

from queue import PriorityQueue
from math import inf

def dijkstra(G,v,s,D,T):

    n = len(G)
    d = [[inf]*D for _ in range(n)]
    d[v][0] = 0
    visited = [[False]*D for _ in range(n)]
    p = [[-1]*D for _ in range(n)]
    K = PriorityQueue()
    K.put((0, v, 0)) # krotka - (dotychczaswoy koszt, wierzchołek, ile l benzyny mam dojezdzajac do wierzchołka)
    while not K.empty():
        u=K.get()
        x = u[0]    # obecny koszt
        y = u[1]    # wierzchołek obecny
        z = u[2]    # l benzyny które mam dojeżdżając
        if y == s:
            return x
        if visited[y][z] is False:
            visited[y][z] = True
            i = 0
            while i+z <= D:
                for v in G[y]:
                    if v[1] <= i+z and d[v[0]][i+z-v[1]] > x + i*T[y]:
                        d[v[0]][i+z-v[1]] = x + i*T[y]
                        p[v[0]][i+z-v[1]] = y
                        K.put((x + i*T[y],v[0],i+z-v[1]))
                i += 1

    return d


A = [
    [(1,3),(4,2),(3,3)],    # 0
    [(0,3),(3,4),(2,5)],    # 1
    [(1,5),(3,2),(7,1)],    # 2
    [(0,3),(1,4),(2,2),(6,4)],  # 3
    [(0,2),(5,3)],      # 4
    [(4,3),(6,4),(8,3)]   ,  # 5
    [(5,4),(3,4),(8,2),(7,3)],  # 6
    [(2,1),(6,3),(8,1)], # 7
    [(5,3),(6,2),(7,1)]  #8

]
T = [1,3,2,2,2,2,4,4,3]
print(dijkstra(A,0,8,5,T))