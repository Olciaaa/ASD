# Prima

# zakładamy że graf jest spójny

from queue import PriorityQueue

def Prima(G):
    n = len(G)
    Q = PriorityQueue()

    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    
    weight = [float('inf') for i in range(n)]
    MST = []
    
   # visited[0] = True
    Q.put([0,0])

    while not Q.empty():

        ver = Q.get()
        w_u, u = ver
        visited[u] = True

        for  v , w in G[u]:

            if not visited[v]:

                if weight[v] >= w:
                    weight[v] = w
                    parent[v] = u
                    Q.put([w,v])

    
    for i in range(1,n):
        MST.append([parent[i],i]) 

    return MST


def Prima2(G,s):
    n = len(G)

    visited = [False for i in range(n)]
    distance = [float('inf') for i in range(n)]
    parents = [None for i in range(n)]
    MST = []
    Q = PriorityQueue()
    # waga(dis), wierzchołek
    Q.put(s)

    while not Q.empty():
        dis_u, u = Q.get()
        visited[u] = True

        for v,dis_v in G[u]:
           
            if not visited[v]:
                if distance[v] >= dis_v:
                    distance[v] = dis_v
                    parents[v] = u
                    Q.put([dis_v,v])

    for i in range(1,n):
        MST.append([parents[i],i])
    
    return MST





graph = [[(1, 1), (2, 3)], [(0, 1), (3, 2), (4, 4)], [(0, 3), (3, 1), (4, 2)], [(1, 2), (2, 1), (5, 1)],
         [(1, 4), (2, 2), (5, 3)], [(3, 1), (4, 3)]]
print(Prima(graph))
print(Prima2(graph,[0,0]))