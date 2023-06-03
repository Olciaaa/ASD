# spojne skladowe

def DFS(G):
    n = len(G)

    visited = [None for i in range(n)]
   
    time_arr = [None for i in range(n)]

    time_v = 0

   


    def DFSrec (G, visited, v, time_arr):
        nonlocal time_v
        visited[v] = True

        for u in G[v]:
            if not visited[u]:
                
                DFSrec(G,visited, u, time_arr)
            
            #time_v += 1
        time_v += 1
        time_arr[v] = time_v
        
    
    for v in range(n):
        if not visited[v]:
            DFSrec(G,visited, v, time_arr)
    
    return time_arr


def new_graph(G):
    n = len(G)
    new_G = [[] for i in range(n)]

    for v in range(n):

        for u in G[v]:

            new_G[u].append(v)
    
    return new_G

def DFS_2(new_G, time_arr):

    n = len(new_G)

    visited = [False for i in range(n)]
    
    def DFSrec2(new_G,u,visited,time_arr_mod):

        visited[u] = True
        

        for v in new_G[u]:
            if not visited[v]:
                visited[v] = True
                DFSrec2(new_G,v,visited,time_arr_mod)
        
    counter = 0

    time_arr_mod = [[0,0] for i in range(n)]

    
    for i in range(n):
        time_arr_mod[i][0], time_arr_mod[i][1] = i, time_arr[i]
    
    time_arr_mod.sort(key = lambda x: x[1], reverse = True )

    
    for i in range(n):
        if not visited[time_arr_mod[i][0]]:
            u = time_arr_mod[i][0]

            DFSrec2(new_G,u,visited,time_arr_mod)
            counter += 1
            
    return counter

    



graph = [[1, 4], [2], [0], [4, 6], [5], [3], [5], [8], [9], [5, 10], [7]]

new_G = (new_graph(graph))
print(new_G)
time_arr = (DFS(graph))
print(time_arr)
print(DFS_2(new_G,time_arr))