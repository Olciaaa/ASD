from zad4ktesty import runtests

def falisz ( T ):
    dynamic = [[-1 for _ in range(len(T))] for _ in range(len(T))]
    #Tutaj proszę wpisać własną implementację

    val = sum_of_fields(T, dynamic, 0, 0)
    #for el in dynamic:print(el)
    return val

def sum_of_fields(T, dynamic, idx_x, idx_y):
    n = len(T)
    if idx_x == idx_y == n - 1:
        return T[idx_y][idx_x]

    if dynamic[idx_y][idx_x] != -1:
        return dynamic[idx_y][idx_x]

    if idx_x == n - 1:
        value = 0
        for i in range(idx_y, n):
            value += T[i][idx_x]
        dynamic[idx_y][idx_x] = value
        return value
    elif idx_y == n - 1:
        value = 0
        for i in range(idx_x, n):
            value += T[idx_y][i]
        dynamic[idx_y][idx_x] = value
        return value

    val = min(sum_of_fields(T, dynamic, idx_x + 1, idx_y), sum_of_fields(T, dynamic, idx_x, idx_y + 1)) + T[idx_y][idx_x]
    dynamic[idx_y][idx_x] = val
    return val

runtests ( falisz )
