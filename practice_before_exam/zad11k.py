from zad11ktesty import runtests

def kontenerowiec(T):
    print(T)
    suma = 0
    for el in T:
        suma += el

    dynamic = [[-1 for _ in range(suma + 1)] for _ in range(len(T))]
    return minimum_wage(T, dynamic, 0, 0)

def minimum_wage(T, dynamic, idx, p):
    if idx == len(T):
        return p

    if dynamic[idx][p] != -1:
        return dynamic[idx][p]

    dynamic[idx][p] = min(minimum_wage(T, dynamic, idx + 1, abs(p - T[idx])), minimum_wage(T, dynamic, idx + 1, abs(p + T[idx])))
    return dynamic[idx][p]

runtests ( kontenerowiec )
    