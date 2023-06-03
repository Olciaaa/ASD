from zad2testy import runtests
import time

def divisionBorder(start, pivot_id, tab):
    border_id = start

    for i in range(start, pivot_id):
        if tab[i][0] < tab[pivot_id][0] or (tab[i][0] == tab[pivot_id][0] and tab[i][1] > tab[pivot_id][1]):
            tab[border_id], tab[i] = tab[i], tab[border_id]
            border_id += 1

    tab[border_id], tab[pivot_id] = tab[pivot_id], tab[border_id]
    return border_id

def quickSort(tab, start, end):
    while start < end:
        border = divisionBorder(start, end, tab)
        quickSort(tab, start, border - 1)
        start = border + 1
    return tab

def depth(L):
    #stTime = round(time.time() * 1000)
    n = len(L)
    quickSort(L, 0, n - 1)

    #timePoint = round(time.time() * 1000) - stTime
    #print("po sorcie: " + str(timePoint))

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

    #timePoint = round(time.time() * 1000) - stTime
    #print("koniec: " + str(timePoint))

    return max
    pass

runtests( depth )