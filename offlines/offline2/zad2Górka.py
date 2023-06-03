from zad2testy import runtests


def quickSort(T, p, r):
    if p < r:
        T[(p + r) // 2], T[p] = T[p], T[(p + r) // 2]
        pivot = T[p][0]
        i = p - 1
        j = r + 1
        while True:
            i += 1
            while T[i][0] < pivot:
                i += 1
            j -= 1
            while T[j][0] > pivot:
                j -= 1
            if i >= j:
                q = j
                break
            T[i], T[j] = T[j], T[i]
        quickSort(T, p, q)
        quickSort(T, q + 1, r)


def depth(L):
    n = len(L)
    quickSort(L, 0, n - 1)
    i = 0
    next_start = 0
    curr_max = 0
    while i < n:
        intervals_start_with_me = 0
        max_start_with_me = L[i][1]
        j = i + 1
        flag = True
        while j < n and L[i][0] == L[j][0]:
            if L[j][1] > max_start_with_me:
                max_start_with_me = L[j][1]
            intervals_start_with_me += 1
            j += 1
        curr = 0
        while j < n and L[j][0] <= max_start_with_me:
            if L[j][1] <= max_start_with_me:
                curr += 1
            elif flag:
                next_start = j
                flag = False
            j += 1
        if curr + intervals_start_with_me > curr_max:
            curr_max = curr + intervals_start_with_me
        if flag:
            next_start = j
        i = next_start
        if i < n:
            while i > 0 and L[i][0] == L[i - 1][0]:
                i -= 1
    return curr_max


runtests(depth)
