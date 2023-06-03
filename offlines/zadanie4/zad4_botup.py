from zad4testy import runtests

def isNotHover(T, idx):
    #elA = T[idx][1]
    elB = T[idx][2]
    for i in range(len(T) - 1, idx, -1):
        if elB >= T[i][1]:
            return False

    '''for i in range(idx - 1, - 1, -1):
        if elA <= T[i][2]:
            return False'''

    return True

def val(element):
    return element[0] * (element[2] - element[1])

def func(T, p):
    n = len(T)
    tab = [[0 for _ in range(p + 1)] for _ in range(n)]

    for i in range(T[0][3], p + 1):
        tab[0][i] = val(T[0])#T[0][0] * (T[0][2] - T[0][1])

    for i in range(p + 1):
        for j in range(1, n):
            tab[j][i] = tab[j - 1][i]

            if (i - T[j][3]) >= 0 and isNotHover(T, j):
                tab[j][i] = max(tab[j][i], tab[j - 1][i - T[j][3]] + val(T[j]))

    print(tab[n - 1][p])
    return []

def select_buildings(T, p):
    # tu prosze wpisac wlasna implementacje
    T.sort(key=lambda x: (x[2], x[1]))
    return func(T, p)

runtests( select_buildings )

#h, a, b, w
#max = 20
#val: [3, 12, 9, 2, 27]
T = [(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
T.sort(key=lambda x: (x[2], x[1]))
#print(select_buildings(T, 40))