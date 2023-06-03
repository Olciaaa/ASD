from zad5ktesty import runtests

def garek (A):
    print(A)
    n = len(A)
    dynamic = [[-1 for _ in range(n)] for _ in range(n)]
    value = recursive(A, dynamic, 0, len(A) - 1)#max(recursive(A, dynamic, 0, len(A) - 1),(recursive(A, dynamic, 0, len(A) - 1)))
    dynamic[0][n - 1] = value
    for el in dynamic:
        print(el)

    return value

def recursive(T, dynamic, idx_start, idx_stop):
    if idx_start > idx_stop:
        return 0

    if dynamic[idx_start][idx_stop] != -1:
        return dynamic[idx_start][idx_stop]

    i_s1 = idx_start + 1
    i_e1 = idx_stop

    val1 = min(recursive(T, dynamic, i_s1 + 1, i_e1), recursive(T, dynamic, i_s1, i_e1 - 1)) + T[idx_start]

    i_s1 = idx_start
    i_e1 = idx_stop - 1

    val2 = min(recursive(T, dynamic, i_s1 + 1, i_e1), recursive(T, dynamic, i_s1, i_e1 - 1)) + T[idx_stop]

    dynamic[idx_start][idx_stop] = max(val1, val2)
    return max(val1, val2)

runtests ( garek )