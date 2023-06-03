'''
Aleksandra Poskróbek

W algorytmie połączyłam Counting, Quick i Bucket Sort. Najpierw wywołuję counting dla tablicy P, sortując ją po początku
przedziału (elementy w niej są od 1 do N, więc sortowanie odbywa się liniowo). Następnie odbywa się sortowanie kubełkowe
na przedziałach, gdzie kubełków jest n * prawdopodobieństwo z tablicy P. Elementy, które już są dodane do kubelkow,
przesuwam na koniec i "zmieniam" długość tablicy T. Kolejne wywołania będą przechodzić po mniejszej ilości elementów,
dzięki czemu czas jest mniejszy, a bez sensu ponownie sortować te same elementy. Rozwiązuje to również problem
nachodzących na siebie przedziałów.

Złożoność czasowa tego programu to O(n), pamięciowa również O(n).
'''

from zad3testy import runtests

def FindBorder(tab, start, pivot):
    border = start
    elPivot = tab[pivot]
    for i in range(start, pivot):
        if elPivot > tab[i]:
            tab[border], tab[i] = tab[i], tab[border]
            border += 1
    tab[border], tab[pivot] = tab[pivot], tab[border]
    return border

def QuickSort(tab, start, pivot):
    while start < pivot:
        border = FindBorder(tab, start, pivot)
        QuickSort(tab, start, border - 1)
        start = border + 1

def BucketSort(tab, numOfBackets, minimum, maximum, n, toReturn):
    sequence = (maximum - minimum) / numOfBackets
    buckets = [[] for _ in range(numOfBackets)]
    i = 0
    while i < n:
        element = tab[i]
        if element >= minimum and element <= maximum:
            bucketId = int((element - minimum) // sequence)
            buckets[bucketId].append(element)
            tab[i], tab[n - 1] = tab[n - 1], tab[i]
            n -= 1
        else: i += 1

    for i in range(numOfBackets):
        lenB = len(buckets[i])
        if lenB > 1: QuickSort(buckets[i], 0, lenB - 1)

    for i in range(numOfBackets):
        bucket = buckets[i]
        for j in range(len(bucket)):
            toReturn.append(bucket[j])

    return toReturn

def CountingSort(P, n):
    lenP = len(P)
    counting = [0 for _ in range(n)]
    sorted = [0 for _ in range(lenP)]

    for el in P:
        counting[el[0]] += 1

    for i in range(1, n):
        counting[i] += counting[i - 1]

    for i in range(lenP - 1, -1, -1):
        sorted[counting[P[i][0]] - 1] = P[i]
        counting[P[i][0]] -= 1

    for i in range(lenP):
        P[i] = sorted[i]

    return P

def SortTab(T,P):
    lenT = len(T)
    CountingSort(P, lenT)
    toReturn = []
    lenR = 0
    i = 0

    while lenR < lenT:
        toReturn = BucketSort(T, int(lenT * (P[i][2])) + 1, P[i][0], P[i][1], lenT - lenR, toReturn)
        lenR = len(toReturn)
        i += 1

    return toReturn

runtests( SortTab )