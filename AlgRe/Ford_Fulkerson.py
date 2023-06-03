# Ford_Fulkerson

from collections import deque


def BFS(G,s,t,parent):

    n = len(G)
    visited = [False for i in range(n)]
    # parent = [None for i in range(n)]
    dis = [0 for i in range(n)]

    Queue = deque()

    Queue.append(s)
    visited[s] = True

    while len(Queue) > 0:

        u = Queue.popleft()

        for v in range(n):
            if (not visited[v]) and G[u][v] != 0:
                visited[v] = True
                parent[v] = u
                dis[v] = dis[u] + 1
                Queue.append(v)
                if v == t:
                    return True
    
  
    return False

def Fulkerson(G,start,end):
    n = len(G)
    parent= [None for i in range(n)]
    for i in range(n):
        print(G[i])
    
    print('----------------------------------------------------------------')

    G_cp = [[G[i][j] for j in range(n)] for i in range(n)]


    max_flow = 0

    while BFS(G_cp,start,end,parent):

        path_flow = float('inf')
        s = end
        while s != start:
            path_flow = min( path_flow, G_cp[parent[s]][s] )
            s = parent[s]
        
        max_flow += path_flow

        v = end

        while v != start:
            u = parent[v]
            G_cp[u][v] -= path_flow
            G_cp[v][u] += path_flow
            v = u
    
    for i in range(n):
        print(G_cp[i])   
    return max_flow

  

graph = [[0, 4, 0, 3, 0, 0],
         [0, 0, 2, 2, 0, 0],
         [0, 0, 0, 0, 0, 4],
         [0, 0, 2, 0, 2, 0],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0]]
s = 0
t = len(graph)-1

print(Fulkerson(graph,s,t))
print('---------------------------')
for i in range(len(graph)):
        print(graph[i])

 