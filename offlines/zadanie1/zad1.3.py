from zad1testy import Node, runtests

def divisionBorder(start, k):
    if (start.next is None or k < 1):
        return 0;
    prev = start
    to_cut_first = None
    to_cut_last = None
    n = 0;

    for i in range(k):
        current = prev.next
        if current is None:
            break
        if current.val >= start.val:
            if to_cut_first is None:
                to_cut_first = current
                to_cut_last = to_cut_first
            else:
                to_cut_last.next = current
                to_cut_last = to_cut_last.next
            prev.next = current.next
            current.next = None
        else:
            n += 1
            prev = current

    if to_cut_first is not None:
        to_cut_last.next = prev.next
        prev.next = to_cut_first

    temp = prev.val
    prev.val = start.val
    start.val = temp
    divisionBorder(start, n)

def sort(start, k, left):
    while start is not None:
        divisionBorder(start, k)
        start = start.next

    #if left == 0 or start.next is None:
    #    return
    #n = divisionBorder(start, left)
    #sort(start, k, n)
    #sort(start.next, k, k)

def SortH(p,k):
    sort(p, k, k)
    return p
    pass
runtests( SortH ) 
