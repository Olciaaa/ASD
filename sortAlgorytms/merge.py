def mergeSort(tab):
    n = len(tab)
    if n > 1:
        border = n // 2
        L = tab[:(border)]
        P = tab[(border):]

        mergeSort(L)
        mergeSort(P)

        id_L = 0
        id_P = 0
        id_tab = 0
        lenL = len(L)
        lenP = len(P)

        while id_L < lenL and id_P < lenP:
            if L[id_L] <= P[id_P]:
                tab[id_tab] = L[id_L]
                id_L += 1
            else:
                tab[id_tab] = P[id_P]
                id_P += 1
            id_tab += 1

        while id_L < lenL:
            tab[id_tab] = L[id_L]
            id_L += 1
            id_tab += 1

        while id_P < lenP:
            tab[id_tab] = P[id_P]
            id_P += 1
            id_tab += 1

tab = [2, 4,6, 7,567,2, 43, 2,1]
mergeSort(tab)
print(tab)