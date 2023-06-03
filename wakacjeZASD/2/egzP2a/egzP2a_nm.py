from egzP2atesty import runtests 
def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def select(A, p, k, r):
    if p == r: return A[p][1]
    if p < r:
        q = partition(A, p, r)
        if q == k: return A[q][1]
        elif q < k: return select(A, q + 1, k, r)
        else: return select(A, p, k, q - 1)

def zdjecie(T, m, k):
    #tutaj proszę wpisać własną implementację
    #print(T)

    start = 0
    currK = k
    for i in range(m - 1):
        select(T, start, currK, len(T) - 1)
        start, currK = currK, 2 * currK - start + 1
    #print(T)
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

#zdjecie([(1, 10),(1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1)], 4, 1)
runtests ( zdjecie, all_tests=True )