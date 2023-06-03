'''
Aleksandra Poskróbek

Stworzyłam tablicę z pozostałym miejscem dla każdego magazynu. Ponieważ każdy transport ma maksymalnie T ton, a pojemności
każdego magazynu to również T, to wystarczyło zrobić tablicę o długości len(A). Dla każdego elementu z tablicy A szukam po
kolei w komórkach magazynu miejsca i gdy je znajdę, to pojemność tej komórki magazynu jest odpowiednio zmniejszana.
'''

from egz2atesty import runtests

def coal( A, T ):
    leftSpace = [T for _ in range(len(A))]
    # tu prosze wpisac wlasna implementacje
    return find(A, leftSpace)

def find(A, leftSpace):
    toRet = 0
    for el in A:
        idx = 0
        while leftSpace[idx] - el < 0:
            idx += 1

        leftSpace[idx] = leftSpace[idx] - el
        toRet = idx

    return toRet

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
