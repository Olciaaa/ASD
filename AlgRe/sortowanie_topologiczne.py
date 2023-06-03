#sortowanie topologiczne


def DFS(G):
    n = len(G)

    visited = [None for i in range(n)]
    sort_top = []

    for u in range(n):
        if not visited[u]:
            DFSrec(G,u,visited,sort_top)
    
    
    sort_top.reverse()

    return sort_top



def DFSrec(G,u,visited,sort_top):

    visited[u] = True
    
    for v in G[u]:
        if not visited[v]:
            visited[v] = True
            DFSrec(G,v,visited,sort_top)
    
    sort_top.append(u)
  

graph = [[1, 2, 5], [2, 4], [], [], [3, 6], [4], []]

print(DFS(graph))
                
            

