import sys
from zad3ktesty import runtests

sys.setrecursionlimit(10**9)
def ksuma(T, k):
    #print(T)
    #print(k)
    dynamic = [-1 for _ in range(len(T))]
    minimum = float('inf')
    for i in range(k):
        value = recursive(T, dynamic, i, k)
        if value < minimum:
            minimum = value
    #for el in dynamic:
        #print(el)
    return minimum

def recursive(T, dynamic, idx, k):
    if idx >= len(T):
        return 0

    minimum = float('inf')
    if dynamic[idx] != -1:
        return dynamic[idx]

    for i in range(idx + 1, min(idx + k + 1, len(T) + 1)):
        local_min = recursive(T, dynamic, i, k)
        if local_min < minimum:
            minimum = local_min
    dynamic[idx] = minimum + T[idx]
    return minimum + T[idx]

print(ksuma([2,4,7], 1))
runtests(ksuma)