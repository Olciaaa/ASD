from kol2btesty import runtests

#NIE ZNIOSE WIECEJ TEGO ZADANIA AAAAAAAAAAAAAAAAAAAAAAAAAA
#K: 0 - odległość, 1 - koszt

def recursion(K, T, L, i, boost, F):

    if K[i][0] + T >= L or (not boost and K[i][0] + 2 * T >= L):
        F[i][boost] = K[i][1]
        return F[i][boost]

    if F[i][boost] != -1:
        return F[i][boost]

    mini = float('inf')
    idx = i + 1
    while idx <= len(K) and K[idx][0] - K[i][0] <= T:
        mini = min(mini, recursion(K, T, L, idx, boost, F))
        idx += 1

    while not boost and idx <= len(K) and K[idx][0] - K[i][0] <= 2 * T:
        mini = min(mini, recursion(K, T, L, idx, 1, F))
        idx += 1

    F[i][boost] = mini + K[i][1]
    return F[i][boost]


def min_cost(O, C, T, L):
    n = len(O)
    F = [[-1 for _ in range(2)] for _ in range(n)]
    K = []
    for i in range(n):
        K.append((O[i], C[i]))
    K.sort(key=lambda x: x[0])
    K.append((L, 0))
    print(K)

    mini = float('inf')
    idx = 0
    while idx <= len(K) and K[idx][0] - K[0][0] <= T:
        mini = min(mini, recursion(K, T, L, idx, 0, F))
        idx += 1

    while idx <= len(K) and K[idx][0] - K[0][0] <= 2 * T:
        mini = min(mini, recursion(K, T, L, idx, 1, F))
        idx += 1

    return mini


runtests(min_cost, all_tests=False)

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25
# Prawidlowy wynik:	 10
print(min_cost(O, C, T, L))
