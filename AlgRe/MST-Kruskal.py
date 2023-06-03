#MST KRUSKAL

class Node:

    def __init__(self,val):
        
        self.parent = self
        self.val = val
        self.rank = 0

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    if x.rank > y.rank:
        y.parent = x
    
    elif y.rank > x.rank:
        x.parent = y
    
    else:
        y.parent = x
        x.rank += 1



def find_vertices(G):

    max_v = -1

    for i in range(len(G)):
        max_v = max(max_v, G[i][0], G[i][1])
    
    return max_v

def Kruskal_MST(G):
    n = len(G)
    result = []

    vertices = find_vertices(G)

    Tab_node = []

    for i in range(vertices +1):
        Tab_node.append(Node(i))

    #G.sort(key = lambda x: x[2])
    
    e = i = 0
    while e < vertices:

        u, v, w = G[i]
        x = find(Tab_node[u])
        y = find(Tab_node[v])
        
        #i += 1

        if x != y:
            e += 1
            result.append(G[i])
            union(Tab_node[u],Tab_node[v])
        i+=1
        
    return result


