from queue import PriorityQueue


def ksuma1( T, k ):
    n = len(T)
    Q = PriorityQueue(n + k)
    for i in range(k):
        Q.insert((0, -i - 1))
    for i in range(n):
        while i - Q.first()[1] > k:
            Q.extract_min()
        top = T[i] + Q.first()[0]
        Q.insert((top, i))
    while n - Q.first()[1] > k:
        Q.extract_min()
    return Q.first()[0]