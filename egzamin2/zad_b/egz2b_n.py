'''
Aleksandra Poskróbek

Mój pomysł opiera się na algorytmie dynamicznym, w którym tablica posiada dwie komórki. Jedna to indeks obecnej komnaty,
a druga to ilość pieniędzy, które obecnie posiada Wojownik. Ponieważ Wojownik nie może wziąć więcej niż 10 sztabek złota,
to w danym momencie będzie mógł mieć maksymalnie 10 * n sztabek. Dlatego program ma złożoność 10n^2, gdzie po redukcji
stałej wychodzi po prostu n^2.

Wojownik może wejść do następnej sali tylko jeżeli posiada wystarczającą ilość pieniędzy, zapisaną w zmiennej "money".
Jego najlepszy zysk z pójścia z obecnie przesiadywanej komnaty jest zwracany i zapisywany w tablicy pod indeksem
[money][obecny_idx]. Jest jeszcze narzucone ograniczenie, że jeżeli miałby wziąć więcej niż 10 sztabek albo miałby oddać
więcej niż ma, to nie wchodzi do komnaty z takimi ograniczeniami.
'''
import sys
from math import inf
from egz2btesty import runtests
sys.setrecursionlimit(1000000)

def magic( C ):
    # tu prosze wpisac wlasna implementacje
    dynamic = [None for _ in range(len(C))]

    return rec(C, dynamic, 0, 0)

def rec(C, dynamic, idx, money):
    if idx == len(C) - 1:
        return 0

    if dynamic[idx] != None:
        return dynamic[idx]

    maximum = - inf
    for i in range(1, len(C[idx])):
        biore = C[idx][0] - C[idx][i][0]
        if C[idx][i][1] != -1 and biore <= 10 and money + biore >= 0:
            maximum = max(maximum, rec(C, dynamic, C[idx][i][1], money + biore) + biore)

    dynamic[idx] = maximum
    return maximum
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
