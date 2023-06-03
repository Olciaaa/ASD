#cykl Eulera

from collections import deque

def euler(G):

    Q = []

    DFS(G,Q,0)
    return Q


def DFS(G,Q,u):

    for v in G[u]:
        if v != None:
            remove(G,u,v)
            DFS(G,Q,v)
    
    Q.append(u)

def remove(G,u,v):

    for a in range(len(G[u])):
        if G[u][a] == v:
            G[u][a] = None
    
    for b in range(len(G[v])):
        if G[v][b] == u:
            G[v][b] = None



def euler2(G):

    res = []

    DFS2(G,res,0)
    return res

def DFS2(G,res,u):
    
    for v in G[u]:
        if v != None:
            remove2(u,v,G)
            DFS2(G,res,v)
    res.append(u)

def remove2(u,v,G):

    for a in range(len(G[u])):
        if G[u][a] == v:
            G[u][a] = None
    
    for b in range(len(G[v])):
            if G[v][b] == u:
                G[v][b] = None

graph = [[1,2], [0,2,3,5], [0,1,3,5], [1,2,4,5], [3,5], [1,2,3,4]]
graph1 = [[1,2], [0,2,3,5], [0,1,3,5], [1,2,4,5], [3,5], [1,2,3,4]]


print(euler(graph))
print(euler2(graph1))
