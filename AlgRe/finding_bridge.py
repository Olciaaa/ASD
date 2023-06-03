#finding bridge




def DFS(G):

    n = len(G)

    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    time_arr = [float('inf') for i in range(n)]
    low_arr = [float('inf') for i in range(n)]
    bridges = []
    
    time_v = 0


    def DFSrec(G,u,visited,parent,bridges,time_arr,low_arr):

        nonlocal time_v
        visited[u] = True
        time_v += 1
        low_arr[u] = time_v
        time_arr[u] = time_v

        for v in G[u]:
            if not visited[v]:
                # visited[v] = True
                parent[v] = u
                DFSrec(G,v,visited,parent,bridges,time_arr,low_arr)

                low_arr[u] = min(low_arr[u],low_arr[v])

            elif visited[v] and parent[u] != v:
                
                low_arr[u] = min(time_arr[u],low_arr[v])
        
        
        #if low_arr[u] == time_arr[u] and low_arr[parent[u]] == time_arr[parent[u]]:
        if low_arr[u] == time_arr[u] and parent[u] != None:
            bridges.append([u,parent[u]])


    for u in range(n):
        if not visited[u]:
            DFSrec(G,u,visited,parent,bridges,time_arr,low_arr)
    
    return bridges


G = [[1,2], [0,3], [0,3,4], [1,2,5], [2], [3,6,7], [5,7], [5,6]]
print(DFS(G))