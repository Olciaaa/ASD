from zad9ktesty import runtests
from math import inf

def prom(P, g, d):
    dynamic = [[[-1 for _ in range(g + 1)] for _ in range(d + 1)] for _ in range(len(P))]
    recursive(P, dynamic, 0, g, d)

    toReturn1 = []
    toReturn2 = []
    idx = 0
    l1 = g
    l2 = d

    while not (idx == len(P) or (l1 - P[idx] < 0 and l2 - P[idx] < 0)):
        if l1 - P[idx] < 0:
            toReturn2.append(idx)
            l2 -= P[idx]
            idx += 1
        elif l2 - P[idx] < 0:
            toReturn1.append(idx)
            l1 -= P[idx]
            idx += 1
        else:
            val1 = dynamic[idx + 1][l2 - P[idx]][l1]
            val2 = dynamic[idx + 1][l2][l1 - P[idx]]

            if val1 >= val2:
                l2 -= P[idx]
                toReturn2.append(idx)
            else:
                l1 -= P[idx]
                toReturn1.append(idx)
            idx += 1

    idx -= 1
    print(toReturn1)
    print(toReturn2)

    if idx in toReturn1:
        return toReturn1

    return toReturn2



def recursive(P, dynamic, idx, left_place_on1, left_place_on2):
    if idx == len(P): return 0

    if dynamic[idx][left_place_on2][left_place_on1] != -1: return dynamic[idx][left_place_on2][left_place_on1]

    if left_place_on1 - P[idx] < 0 and left_place_on2 - P[idx] < 0:
        return 0

    if left_place_on1 - P[idx] < 0:
        dynamic[idx][left_place_on2][left_place_on1] = recursive(P, dynamic, idx + 1, left_place_on1, left_place_on2 - P[idx]) + 1
        return dynamic[idx][left_place_on2][left_place_on1]
    if left_place_on2 - P[idx] < 0:
        dynamic[idx][left_place_on2][left_place_on1] = recursive(P, dynamic, idx + 1, left_place_on1 - P[idx], left_place_on2) + 1
        return dynamic[idx][left_place_on2][left_place_on1]

    dynamic[idx][left_place_on2][left_place_on1] = max(recursive(P, dynamic, idx + 1, left_place_on1 - P[idx], left_place_on2), recursive(P, dynamic, idx + 1, left_place_on1, left_place_on2 - P[idx])) + 1
    return dynamic[idx][left_place_on2][left_place_on1]
T = [5, 6, 1, 3, 2, 4, 3, 5]
l1 = 8
l2 = 10
#print(prom(T, l1, l2))
runtests ( prom )