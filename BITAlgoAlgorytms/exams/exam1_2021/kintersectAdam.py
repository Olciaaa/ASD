import math

from zad3testy import runtests


def kintersect(A, k):
    n = len(A)
    S = [-1 for _ in range(n * 2)]

    for i in range(n):
        S[i] = (A[i][0], A[i][1], True, i)
        S[i + n] = (A[i][1], A[i][0], False, i)

    S.sort(key=lambda x: x[0])

    count = 0
    curr = []
    best = 0
    result_t = [None for _ in range(k)]

    def find_max(curr, checking):
        max_val = 0
        max_tuple = None
        for elem in curr:
            if elem[1] == checking and elem[0] >= max_val:
                max_val = elem[0]
                max_tuple = elem
        return max_tuple

    for i in range(2 * n):
        if S[i][2]:
            count += 1
            curr.append(S[i])
        else:
            count -= 1
            find = (S[i][1], S[i][0], True, S[i][3])
            curr.remove(find)
            if len(curr) >= k:
                end = min(curr[:k], key=lambda x: x[1])
                start = max(curr[:k], key=lambda x: x[0])
                lenght = end[1] - start[0]
                if lenght > best:
                    best = lenght
                    for j in range(k):
                        result_t[j] = curr[j]
        if count == k:
            end = min(curr, key=lambda x: x[1])
            start = max(curr, key=lambda x: x[0])
            lenght = end[1] - start[0]
            if lenght > best:
                best = lenght
                for j in range(k):
                    result_t[j] = curr[j]

    for i in range(k):
        result_t[i] = result_t[i][3]
    return result_t


runtests(kintersect)
