'''
Aleksandra Poskróbek

Algorytm na początku znajduje n i obraca słowa jeżeli najmniejsza litera jest na koncu. Następnie sortuje radixem + countem
elementy tablicy, dzięki czemu takie same słowa będą pod sobą. Następnie jedynie szuka ile słów takich samych jest obok siebie

Złożonść czasowa to O(NlogN), a pamięciowa jest liniowa

'''

from kol1atesty import runtests

def flip(word):
    lastLetter = word[len(word) - 1]
    if ord(word[0]) < ord(lastLetter):
        return word

    flipped = ""
    for i in range(len(word) - 1, -1, -1):
        flipped += word[i]
    return flipped

def sortByPos(tab, el):
    flag = False
    n = len(tab)
    max_el = 26
    counts = [0 for _ in range(max_el)]
    sorted = [0 for _ in range(n)]

    for i in range(n):
        counts[ord(tab[i][el]) - 97] += 1

    for i in range(1, max_el):
        counts[i] += counts[i - 1]

    for i in range(n - 1, -1, -1):
        sorted[counts[ord(tab[i][el]) - 97] - 1] = tab[i]
        counts[ord(tab[i][el]) - 97] -= 1

    for i in range(len(tab)):
        tab[i] = sorted[i]
    return sorted, flag

def maxLen(tab):
    maximum = 0

    for i in range(len(tab)):
        tab[i] = flip(tab[i])
        if len(tab[i]) > maximum:
            maximum = len(tab[i])

    for i in range(len(tab)):
        for j in range(len(tab[i]), maximum):
            tab[i] += "a"

    return maximum

def sortWords(tab, maximum):
    for i in range(maximum - 1, -1, -1):
        sortByPos(tab, i)

def g(T):
    maximum = 0
    maxL = maxLen(T)
    sortWords(T, maxL)
    curr = 1

    for i in range(len(T) - 1):

        if T[i] == T[i + 1]:
            curr += 1
        else:
            if curr > maximum:
                maximum = curr
            curr = 1
    if curr > maximum:
        maximum = curr

    return maximum

runtests( g, all_tests=True )
#print("string" + "0")

