from zad2testy import runtests

def divisionBorder(start, pivot_id, tab, el):
    border_id = start
    last_same = border_id

    for i in range(start, pivot_id):
        if (el == 0 and tab[i][el] < tab[pivot_id][el]) or (el == 1 and tab[i][el] > tab[pivot_id][el]):
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
        if el == 0: quickSort(tab, border, last_same, 1)#sort_same_partitions(tab, border, last_same)
        start = last_same + 1
    return tab

def sort_same_partitions(L: list, l: int, r: int):
    for i in range(l, r):
        if L[i][1] < L[i + 1][1]:
            L[i], L[i + 1] = L[i + 1], L[i]

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

tab = [[1, 2],[1, 5],[1, 2],[1, 3],[1, 4]]
#quickSort(tab, 0, len(tab) - 1, 0)
#print(tab)