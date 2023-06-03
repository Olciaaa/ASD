#DFS

def DFS(G):
    n = len(G)

    visited = [None for i in range(n)]
    parents = [None for i in range(n)]
    time_arr = [None for i in range(n)]
    

    time_v = 0

   


    def DFSrec (G, visited, parents, v, time_arr):
        nonlocal time_v
        visited[v] = True

        for u in G[v]:
            if not visited[u]:
                parents[u] = v
                #visited[v] = True
                DFSrec(G,visited, parents, u, time_arr)
            
            #time_v += 1
        time_v += 1
        time_arr[v] = time_v
        
    
    for v in range(n):
        if not visited[v]:
            DFSrec(G,visited,parents, v, time_arr)
    
    return time_arr



def DFS2(G,s):
    n = len(G)

    visited = [False for i in range(n)]
    distance = [-1 for i in range(n)]
    parents = [None for i in range(n)]
    time_arr = [None for i in range(n)]
    distance[s] = 0
    time_v = 0

    def recDFS2(G,visited,distance,parents,u,time_arr):
        nonlocal time_v
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                distance[v] = distance[u] + 1
                parents[v] = u
                recDFS2(G,visited,distance,parents,v,time_arr)
        time_v += 1
        time_arr[u] = time_v
    
    for u in range(n):
        if not visited[u]:
            recDFS2(G,visited,distance,parents,u,time_arr)
    
    return time_arr , distance



#graph = [[1, 2, 5], [2, 4], [], [], [3, 6], [4], []]
graph = [ [1], [2,4], [0,9], [4,6], [5], [], [5], [9], [7,3], [10], [8,5]]
G = [[1,6], [0,2], [1,3,6], [2,4,5], [3,5], [3,4], [0,2,7], [6]]
print(DFS(G))

t,d = DFS2(G,0)
print(t,d)