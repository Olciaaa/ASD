from queue import PriorityQueue

from egzP4atesty import runtests

def mosty ( T ):
    dynamic = [[-1 for _ in range(len(T))] for _ in range(len(T))]
    print(T)
    newT = []
    T.sort(key = lambda x: x[0])
    for i in range(len(T)):
        newT.append([i, T[i][1]])

    newT.sort(key = lambda x: x[1])
    for i in range(len(T)):
        newT[i][1] = i

    newT.sort(key = lambda x: x[0])
    print(newT)
    #tutaj proszę wpisać własną implementację
    print()
    maximum = 0
    for i in range(1, len(T)):
        maximum = max(longestRising(newT, dynamic, i, i - 1) + 1, maximum)

    return maximum

def longestRising(T, dynamic, lastIdx):
    if lastIdx == len(T):
        return 0

    q = PriorityQueue()

runtests ( mosty, all_tests=True )