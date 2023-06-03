from zad2testy import runtests

def divisionBorder(start, pivot_id, tab, el):
    border_id = start
    last_same = border_id

    for i in range(start, pivot_id):
        if tab[i][el] < tab[pivot_id][el]:
            tab[last_same], tab[i] = tab[i], tab[last_same]
            tab[border_id], tab[last_same] = tab[last_same], tab[border_id]
            border_id += 1
            last_same += 1
        elif tab[i][el] == tab[pivot_id][el]:
            tab[last_same], tab[i] = tab[i], tab[last_same]
            last_same += 1

    tab[last_same], tab[pivot_id] = tab[pivot_id], tab[last_same]
    return border_id, last_same

def quickSort(tab, start, end, el):
    while start < end:
        border, last_same = divisionBorder(start, end, tab, el)
        quickSort(tab, start, border - 1, el)
        bubble(tab, border, last_same)
        start = last_same + 1
    return tab

def bubble(L, l, r):
    max = L[l][1]
    max_id = l
    for i in range(l + 1, r + 1):
        if max < L[i][1]:
            max = L[i][1]
            max_id = i
    L[max_id], L[l] = L[l], L[max_id]

def depth(L):
    n = len(L)
    quickSort(L, 0, n - 1, 0)
    flags = [1 for _ in range(n)]
    max = 0
    for i in range(n):
        if flags[i] == 1:
            current = 0
            element = L[i][1]
            for j in range(i + 1, n):
                if element >= L[j][1]:
                    current += 1
                    flags[j] = 0
                if current > max:
                    max = current
    return max
    pass

runtests( depth )

tab = [[2,3],[1, 2],[1, 5],[1, 2],[1, 3],[1, 4]]
#sort_same_partitions(tab, 2, 4)
#bubble(tab, 0, len(tab) - 1)
#print(tab)
#quickSort(tab, 0, len(tab) - 1, 0)
#print(tab)

#tab = [2, 4, 6, 4, 5, 7, 1]
#depth(tab)
#print(tab)