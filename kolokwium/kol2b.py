from math import inf

from kol2btesty import runtests
def border(tab1, tab2, start, pivot):
    elAfterBorder = start

    for i in range(start, pivot):
        if tab1[i] < tab1[pivot]:
            tab2[i], tab2[elAfterBorder] = tab2[elAfterBorder], tab2[i]
            tab1[i], tab1[elAfterBorder] = tab1[elAfterBorder], tab1[i]
            elAfterBorder += 1

    tab1[pivot], tab1[elAfterBorder] = tab1[elAfterBorder], tab1[pivot]
    tab2[pivot], tab2[elAfterBorder] = tab2[elAfterBorder], tab2[pivot]
    return elAfterBorder

def quickSort(tab1, tab2, start, end):
    while start < end:
        pivot = border(tab1, tab2, start, end)
        quickSort(tab1, tab2, start, pivot - 1)
        start = pivot + 1
    return tab1

def min_cost( O, C, T, L ):
    quickSort(O, C, 0, len(O) - 1)
    dynamic = [[-1 for _ in range(len(O))] for _ in range(3)]

    idx = 0
    minimum = inf
    while idx < len(O) and O[idx] <= T:
        minimum = min(minimum, rec(dynamic, O, C, T, L, idx, 1))
        idx += 1

    while idx < len(O) and O[idx] <= 2 * T:
        minimum = min(minimum, rec(dynamic, O, C, T, L, idx, 0))
        idx += 1

    return minimum

def rec(dynamic, O, C, T, L, i, can_more):
    if T + O[i] >= L or (can_more == 1 and 2 * T + O[i] >= L):
        dynamic[can_more][i] = C[i]
        return C[i]

    if dynamic[can_more][i] != -1:
        return dynamic[can_more][i]

    idx = i + 1
    minimum = inf
    while idx < len(O) and O[idx] <= T + O[i]:
        minimum = min(minimum, rec(dynamic, O, C, T, L, idx, can_more))
        idx += 1
    if can_more == 1:
        while idx < len(O) and O[idx] <= 2 * T + O[i]:
            minimum = min(minimum, rec(dynamic, O, C, T, L, idx, 0))
            idx += 1
    dynamic[can_more][i] = minimum + C[i]
    return minimum + C[i]

runtests( min_cost, all_tests = True )
