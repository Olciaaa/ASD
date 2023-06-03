from zad1testy import Node, runtests
def heapify(tab, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    min_ind = i

    if left < n and tab[left] < tab[min_ind]:
        min_ind = left
    if right < n and tab[right] < tab[min_ind]:
        min_ind = right
    if min_ind != i:
        tab[i], tab[min_ind] = tab[min_ind], tab[i]
        heapify(tab, n, min_ind)

def buildHeap(tab):
    n = len(tab)
    parent = (n - 2)//2
    for i in range(parent, -1, -1):
        heapify(tab, n, i)

def sort(start, k):
    sorted_start = None
    sorted_last = sorted_start
    tab = []
    curr = start

    actual_k = 0
    while curr is not None and actual_k < k + 1:
        tab.append(curr.val)
        curr = curr.next
        #if curr is not None:
        actual_k += 1
    #print(actual_k)
    buildHeap(tab)

    while curr is not None:
        el = Node()
        el.val = tab[0]
        if sorted_start == None:
            sorted_last = el
            sorted_start = sorted_last
        else:
            sorted_last.next = el
            sorted_last = sorted_last.next

        tab[0] = curr.val
        curr = curr.next
        heapify(tab, len(tab), 0)

    for i in range(actual_k - 1, 0, -1):
        el = Node()
        el.val = tab[0]
        if sorted_start == None:
            sorted_last = el
            sorted_start = sorted_last
        else:
            sorted_last.next = el
            sorted_last = sorted_last.next

        tab[0] = tab[i]
        heapify(tab, i, 0)
    el = Node()
    el.val = tab[0]
    sorted_last.next = el

    return sorted_start

def toList(tab):
    first = None
    last = None
    for i in range(len(tab)):
        el = Node()
        el.val = tab[i]
        if first == None:
            first = el
            last = el
        else:
            last.next = el
            last = last.next
    return first

def printList(start):
    toPrint =""
    current = start
    while current is not None:
        toPrint += str(current.val) + " "
        #print(current.val)
        current = current.next
    print(toPrint)

tab = [2, 6, 6, 10, 29, 24, 31, 43, 36, 45, 51, 49, 52, 56, 53, 56, 61, 58, 71, 75, 72, 79, 93, 82, 99]
k = 0
#start = toList(tab)
#print("przed")
#printList(start)
#start = sort(start, k)
#print("po")
#printList(start)

def SortH(p,k):
    p = sort(p, k)
    return p
    pass
runtests( SortH )
