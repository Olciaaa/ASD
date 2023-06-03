from Exercise_1_tests import runtests
def setBorder(tab, start, pivot, n):
    border = start

    for i in range(start, pivot):
        if tab[i//n][i % n] < tab[pivot//n][pivot % n]:
            tab[border//n][border % n], tab[i//n][i % n] = tab[i//n][i % n], tab[border // n][border % n]
            border += 1
    tab[border // n][border % n], tab[pivot//n][pivot % n] = tab[pivot//n][pivot % n], tab[border // n][border % n]
    return border

def quickSelect(tab, start, end, i, n):
    if start >= end:
        return

    pivot = setBorder(tab, start, end, n)
    if pivot == i:
        return

    elif i < pivot:
        quickSelect(tab, start, pivot - 1, i, n)

    else:
        quickSelect(tab, pivot + 1, end, i, n)

def Median(T):
    n = len(T)

    toReturn = []
    interval = int((n * n - n) / 2)
    left_id = 0
    middle_id = interval
    right_id = interval + n

    quickSelect(T, 0, n * n - 1, middle_id, n)
    quickSelect(T, middle_id + 1, n * n - 1, right_id, n)
    print(T)

    for i in range(n):
        tab = []
        for j in range(n):
            if i > j:
                tab.append(T[left_id // n][left_id % n])
                left_id += 1
            elif i == j:
                tab.append(T[middle_id // n][middle_id % n])
                middle_id += 1
            else:
                tab.append(T[right_id // n][right_id % n])
                right_id += 1

        toReturn.append(tab)

    for i in range(n):
        for j in range(n):
            T[i][j] = toReturn[i][j]
    return T

runtests(Median)

'''
tab =  [ [ 98, 23, 5],
[ 7,11,13],
[17,19,23] ]

quickSelect(tab, 0, 8, 3, 3)

print(tab)
'''