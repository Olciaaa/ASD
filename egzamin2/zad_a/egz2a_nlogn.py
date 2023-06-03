from queue import PriorityQueue

from egz2atesty import runtests

def coal( A, T ):
    leftSpace = PriorityQueue()
    for i in range(len(A)):
        leftSpace.put((T, i))
    return -1

def find(A, leftSpace):
    for el in A:
        leftSpace.get()

    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = False )
