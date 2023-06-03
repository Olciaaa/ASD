'''
Aleksandra Poskróbek

Mój kod działa na bazie rekurencji.

Na początku sortuję tablicę T po elementach a (rosnąco), dzięki czemu w rekurencji mając obecny indeks i dane dotyczące
b, to w przypadku gdy go nie biorę elementu to sprawdzam dalsze elementy od indeksu następnego, a jeżeli biorę obecny
element, to sprawdzam od następnego elementu, którego a jest większe niż obecne b, ponieważ b jest prawą stroną dotychczas
zbudowanego miasta. Dynamika polega tu na tym, że wprowadziłam tablicę n x p wypełnioną -1 i jeżeli wartość dla danego
mieszkania nie jest jeszcze policzona, to dodaję tą wartość do tablicy. Jeżeli znam już najlepszą możliwą wartość dla elementu,
czyli tablica dla danego p i idx jest różna od -1, to zwracam tą wartość. Dzięki temu nie liczę wielokrotnie wartości dla
tych samych elementów. Wypisywanie wyniku odbywa się na bazie tablicy dynamicznej, z której po odpowiednich obserwacjach wydobyłam wynik.

Algorytm ma złożoność czasową n^2 + np, a pamięciową np
'''

from zad4testy import runtests
def border(tab, start, pivot, indexes):
    elAfterBorder = start

    for i in range(start, pivot):
        if tab[i][1] < tab[pivot][1] or (tab[i][1] == tab[pivot][1] and tab[i][2] < tab[pivot][2]):
            tab[i], tab[elAfterBorder] = tab[elAfterBorder], tab[i]
            indexes[i], indexes[elAfterBorder] = indexes[elAfterBorder], indexes[i]
            elAfterBorder += 1

    tab[pivot], tab[elAfterBorder] = tab[elAfterBorder], tab[pivot]
    indexes[pivot], indexes[elAfterBorder] = indexes[elAfterBorder], indexes[pivot]
    return elAfterBorder

def quickSort(tab, start, end, indexes):
    while start < end:
        pivot = border(tab, start, end, indexes)
        quickSort(tab, start, pivot - 1, indexes)
        start = pivot + 1
    return indexes

def val(element):
    return element[0] * (element[2] - element[1])

def find_maximum(T, idx, p, dynamic):
    if dynamic[idx][p] != -1:
        return dynamic[idx][p]

    if idx >= len(T):
        return 0

    if p - T[idx][3] < 0:
        dynamic[idx][p] = find_maximum(T, idx + 1, p, dynamic)
        return dynamic[idx][p]

    next_idx = len(T)
    for i in range(idx + 1, len(T)):
        if T[idx][2] < T[i][1]:
            next_idx = i
            break

    dynamic[idx][p] = max(find_maximum(T, next_idx, p - T[idx][3], dynamic) + val(T[idx]), find_maximum(T, idx + 1, p, dynamic))
    return dynamic[idx][p]

def select_buildings(T,p):
    n = len(T)
    dynamic = [[-1 for _ in range(p + 1)] for _ in range(n + 1)]
    ids = [i for i in range(n)]

    quickSort(T, 0, n - 1, ids)
    maximum = find_maximum(T, 0, p, dynamic)
    tab = []

    idx = p
    value = 0
    last_val = dynamic[0][idx]
    right = -1
    for i in range(0, n):
        if idx < 0 or value == maximum: break
        siup = dynamic[i][idx]
        if(siup != dynamic[i + 1][idx]) and T[i][1] > right and last_val == siup:
            last_val = siup - val(T[i])
            tab.append(ids[i])
            value += val(T[i])
            idx -= T[i][3]

            right = T[i][2]

    return tab

runtests( select_buildings )