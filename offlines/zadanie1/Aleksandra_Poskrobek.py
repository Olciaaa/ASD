'''
Aleksandra Poskróbek

Algorytm ma złożoność nlogk, a w przypadku k = 1 złożoność n :). Wywnioskowałam to na podstawie testów i analizie
złożoności funkcji heapify oraz sort.

Sortowanie odbywa się na bazie odwróconego kopca (rodzice są mniejsi niż dzieci).
Algorytm działa w ten sposób, że przepisuje do tablicy k + 1 elementów i jest z nich budowany kopiec,po czym element
na górze kopca ustępuje miejsca następnemu elementowi w liście,  który jeszcze nie dostał się do tablicy (k + 1 indeks
elementu). Pierwszy element zanim opuści pierwszą pozycję, zostaje umieszczony w posortowanej liście. Ostatecznie
algorytm musi jeszcze przejść po pozostałych elementach (jest ich k - 1) i kopcowo je posortować :)

Dodatkowo jest sprawdzane to, czy k nie jest za duże. Dzieje się to w momencie przepisywania elementów do listy, dlatego
nie wpływa zbytnio na złożoność czasową.

W przypadku k = 1 znaczne wydajniejszym jest przejście jednej pętli bubbleSorta, gdyż złożoność w tym wypadku jest
liniowa. Stąd zastosowałam w kodzie taki wyjątek, znacznie polepszający czas pracy algorytmu.

k = O(1) = n
k = O(logn) = n * log(logn)
k = O(n) = n * log(n)
'''

from zad1testy import Node, runtests
def heapify(tab, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    min_ind = i

    if left < n and tab[left].val < tab[min_ind].val:
        min_ind = left
    if right < n and tab[right].val < tab[min_ind].val:
        min_ind = right
    if min_ind != i:
        tab[i].val, tab[min_ind].val = tab[min_ind].val, tab[i].val
        heapify(tab, n, min_ind)

def buildHeap(tab, n):
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
        tab.append(curr)
        curr = curr.next
        actual_k += 1

    buildHeap(tab, actual_k)

    while curr is not None:
        el = tab[0]
        el.next = None
        if sorted_start == None:
            sorted_last = el
            sorted_start = sorted_last
        else:
            sorted_last.next = el
            sorted_last = sorted_last.next

        tab[0] = curr
        curr = curr.next
        heapify(tab, actual_k, 0)

    for i in range(actual_k - 1, 0, -1):
        el = tab[0]
        el.next = None
        if sorted_start == None:
            sorted_last = el
            sorted_start = sorted_last
        else:
            sorted_last.next = el
            sorted_last = sorted_last.next

        tab[0] = tab[i]
        heapify(tab, i, 0)
    el = tab[0]
    el.next = None
    sorted_last.next = el

    return sorted_start

def bubbleSort(p):
    prev = p
    current = p.next

    while current is not None:
        if prev.val > current.val:
            prev.val, current.val = current.val, prev.val
        prev = current
        current = current.next

def SortH(p,k):
    if k <= 0:
        return p
    if k == 1:
        bubbleSort(p)
        return p
    p = sort(p, k)
    return p
    pass
runtests( SortH )