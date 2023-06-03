from egzP2atesty import runtests 

def zdjecie(T, m, k):
    #tutaj proszę wpisać własną implementację
    T.sort(key=lambda x: (x[1], x[0]))
    #print(T)
    rows = [[]for _ in range(m)]
    start = 0
    end = k
    for i in range(m):
        for j in range(start, end):
            rows[i].append(T[j])

        start, end = end, end + (end - start) + 1
    rows.reverse()
    #print(rows)

    row = 0
    el = 0
    for i in range(len(T)):
        if len(rows[row]) == el:
            row = 0
            m -= 1
            el += 1
        T[i] = rows[row][el]
        row += 1
        if row == m:
            row = 0
            el += 1
    #print(T)

    return None

zdjecie([(1, 10),(1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1)], 4, 1)
runtests ( zdjecie, all_tests=True )