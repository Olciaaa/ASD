#BST

class BSTNode:
    def __init__(self,val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None


def insert(root,key):

    p = root
    q = None

    while p != None:

        if p.val < key:
            
            p.parent = q
            q = p

            p = p.right
            
        
        elif p.val > key:
            
            p.parent = q
            q = p
            p = p.left
        else:
            return
    
    p = q
    if p.val > key:
        p.left = BSTNode(key)
        p.left.parent = q
    else:
        p.right = BSTNode(key)
        p.right.parent = q

def buid_tree(T):
    root = BSTNode(100)

    for v in T:
        insert(root,v)
    return root

def find(root,key):

    while root != None:
        if root.val == key:
            return root
        elif root.val > key:
            root = root.right
        else:
            root.left
    return None


def find_min(root):
    p = root
    q = None
    while p != None:
        q = p
        p = p.left
    return q

def find_max(root):
    p = root
    q = None
    while p != None:
        q = p
        p = p.right
    return q

def następnik(root,key):
    p = find(root,key)
    return find_min(p.right)

def poprzednik(root,key):
    p = find(root,key)
    return find_max(p.left)

def remove(root,key):
    to_remove = find(root,key)
    # brak dzieci
    if to_remove.left == None and to_remove.right == None:
            prev = to_remove.parent 

            if prev.left == to_remove:
                prev.left = None
                return
            else:
                prev.right = None
                return
    # jedno dziecko
    elif to_remove.left == None and to_remove.right != None: 
            prev = to_remove.parent    

            if prev.left == to_remove:
                prev.left = to_remove.right
                to_remove.right.parent = prev
                return
            else:
                prev.right = to_remove.right 
                to_remove.right.parent = prev
                return
    
    elif to_remove.right == None and to_remove.left != None:
            prev = to_remove.parent    

            if prev.left == to_remove:
                prev.left = to_remove.lefy
                to_remove.left.parent = prev
                return
            else:
                prev.right = to_remove.left 
                to_remove.left.parent = prev
                return
    
    else:
        to_change = find_min(to_remove.right)
        prev = to_change.parent    
        
        if prev.left == to_change:
                prev.left = None
                
        else:
            prev.right = None
        
        to_change.parent = to_remove.parent
        to_change.left = to_remove.left
        to_change.right = to_remove.right
                

        


        
        
tab = [20,50,35,7,200,250,500,1000,100,75,900]    
buid_tree(tab)    





