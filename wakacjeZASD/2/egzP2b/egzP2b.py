from egzP2btesty import runtests
from math import log10

def countingSort(tab, idx):
    C = [0 for _ in range(2)]
    B = [0 for _ in range(len(tab))]

    for el in tab:
        C[int(el[0][idx])] += 1
    for i in range(1, 2):
        C[i] = C[i] + C[i-1]
    for i in range(len(tab)-1, -1, -1):
        B[C[int(tab[i][0][idx])] - 1] = tab[i]
        C[int(tab[i][0][idx])] -= 1
    for i in range(len(tab)):
        tab[i] = B[i]

def radix(D):
    maxLen = 0
    for el in D:
        if maxLen < len(el):
            maxLen = len(el)

    for idx in range(len(D)):
        D[idx] = [D[idx], D[idx]]

    for idx in range(len(D)):
        for i in range(len(D[idx][0]), maxLen):
            D[idx][0] = "0" + D[idx][0]

    for i in range(maxLen):
        countingSort(D, i)

def binToDec(data):
    dataValue = 0
    pover = 0
    for i in range(len(data) - 1, -1, -1):
        dataValue += int(data[i]) * (2 ** pover)
        pover += 1
    return dataValue

def find(data, D):
    dataValue = binToDec(data)
    idx = None

    left = 0
    right = len(D) - 1
    while left < right:
        if binToDec(D[right][1][len(D[right][1]) - len(data):len(D[right][1])]) == dataValue and binToDec(D[left][1][len(D[left][1]) - len(data):len(D[left][1])]) == dataValue:
            #print(data)
            #print("left " + str(left))
            #print("right " + str(right))
            break
        middle = (left + right) // 2
        if len(D[middle][1]) < len(data) or binToDec(D[middle][1][len(D[middle][1]) - len(data):len(D[middle][1])]) < dataValue:
            left = middle + 1
        else: right = middle
    if binToDec(D[right][1][len(D[right][1]) - len(data):len(D[right][1])]) == dataValue:
        idx = right
    return idx


def bisect_left(self, a, x):
    '''returns i where all a[:i] is less than x'''
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right(self, a, x):
    '''returns i where all a[:i] is less than or equal to x'''
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo

def kryptograf( D, Q ):    
    #tutaj proszę wpisać własną implementację
    radix(D)
    #print(D)
    variations = 0
    print(D)

    for el in Q:
        if len(el) == 0:
            variations += len(D)
        else:
            idx = find(el, D)
            #print(idx)
            if idx is not None:
                variations *= len(D) - 1 - idx
    return 0

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
#runtests(kryptograf, all_tests = 2)
D = ["1100", "100", "0", "1111", "1101"]
Q = ["", "1", "11", "0", "1101"]
kryptograf(D, Q)