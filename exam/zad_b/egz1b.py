from queue import Queue

'''
Pomysl był taki, że chcialam znaleźć średnicę drzewa, a następnie środek drzewa. Z niego należałoby poucinać krawędzie 
do napotkania wierzchołka A lub napotkania na koniec drzewa
'''

from egz1btesty import runtests
parent = []
class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None        # pole do wykorzystania przez studentow

def wideentall( T ):
    # tu prosze wpisac wlasna implementacje
    size = bfs(T)
    #
    G = [[] for _ in range(size + 1)]
    fill(T, 0, 0, G)

    maximum_idx = 0
    maximum = 0
    distance = bfs1(G, 0)
    #print(G)
    for i in range(len(G)):
        if maximum < distance[i]:
            maximum_idx = i
            maximum = distance[i]
    diameter = bfs1(G, maximum_idx)
    print(diameter)

   # print(G)

def bfs1(G, s):
    q = Queue()
    visited = [False for _ in range(len(G))]
    distance = [-1 for _ in range(len(G))]

    visited[s] = True
    distance[s] = 0
    q.put(0)

    while not q.empty():
        u = q.get()
        #print(u)

        for el in G[u]:
            if visited[el] == False:
                #print(el)
                distance[el] = distance[u] + 1
                visited[el] = True
                q.put(el)
    return distance

def bfs(G):
    q = Queue()
    q.put(G)
    size = 0

    while not q.empty():
        u = q.get()

        if u.right is not None:
            q.put(u.right)
        if u.left is not None:
            q.put(u.left)
        size += 1
    return size

def fill(curr, val, idx, G):
    if curr is None:
        return val
    curr.x = val
    #print(val)
    if curr.left is not None:
        G[idx].append(idx + 1)
        G[idx + 1].append(idx)
    if curr.right is not None:
        G[idx].append(idx + 2)
        G[idx + 2].append(idx)
    fill(curr.left, val + 1, idx + 1, G)
    fill(curr.right, val + 1, idx + 2, G)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )