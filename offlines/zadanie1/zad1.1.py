from zad1testy import Node, runtests

def minimum(start, k):
    minn = start.val
    min_el = start
    curr = start
    i = 0
    while curr is not None and i < k+1:
        if minn > curr.val:
            min_el = curr
            minn = curr.val
        curr = curr.next
        i+=1

    temp = start.val
    start.val = minn
    min_el.val = temp

def bubbleSort(p):
    prev = p
    current = p.next

    while current is not None:
        if prev.val > current.val:
            prev.val, current.val = current.val, prev.val
        prev = current
        current = current.next

def SortH(p,k):
    #if k == 1:
    #    bubbleSort(p)
    #    return p
    curr_start = p
    while curr_start is not None:
        minimum(curr_start, k)
        curr_start = curr_start.next

    return p
    pass
runtests( SortH ) 
