def idx(A, l, r, key):
    while (r - l > 1):
        m = l + (r - l) // 2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r

def longestIncreasingSubsequence(T):
    n = len(T)
    S = []
    A = []

    S.append(T[0])

    for i in range(1, n):
        if T[i] >= S[len(S) - 1]:
            S.append(T[i])
        else:
            S[idx(S, -1, len(S) - 1, T[i])] = T[i]
    return len(S)

print(longestIncreasingSubsequence([0,34,5,6,7,3,2,6,8,3,10]))