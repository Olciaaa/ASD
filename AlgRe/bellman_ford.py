#bellman ford

#najkrótsze scieżki jesli wagi mogą być ujemne



def relax(u,v,w,parent,distance):

    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        parent[v] = u

def get_ver(G):
    best_ver = -1
    for i in range(len(G)):
        best_ver = max(best_ver,G[i][0],G[i][1])
    
    return best_ver




def Bellman_ford(G):

    n = get_ver(G)+1
    
    visited = [False for i in range(n)]
    distance = [float('inf') for i in range(n)]
    parent = [None for i in range(n)]

    s = 2

    distance[s] = 0

    for i in range(n):

        for edg in G:
            u,v,w = edg
            if not visited[v]:
                relax(u,v,w,parent,distance)

    for edg in G:
        u,v,w = edg

        if distance[v] > distance[u] + w:
            return 'ma cykl spierdalaj'
        else:
            return distance




def BelmanFord(G,s):

    n = get_ver(G)+1

    visited = [False for i in range(n)]
    distance = [float('inf') for i in range(n)]

    distance[s] = 0

    for _ in range(n):
        for edge in G:
            u,v,w = edge
            if not visited[v]:
                #relax
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
    for edge in G:
        u,v,w = edge
        if distance[v] > distance[u] + w:
            return False
        else:
            return distance
                    


graph = [[0,1,1],[0,7,2],[1,0,1],[1,2,2],[1,4,3],[2,1,2],[2,3,5],[3,2,5],[3,6,1],[4,1,3],[4,5,3],[4,7,1],[5,4,3],
        [5,6,8],[5,8,1],[6,3,1],[6,5,8],[6,8,4],[7,0,2],[7,4,1],[7,8,7],[8,5,1],[8,6,4],[8,7,7]]

print(Bellman_ford(graph))
print(BelmanFord(graph,2))
            
        
        
    


   

