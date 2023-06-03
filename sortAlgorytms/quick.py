def border(tab, start, pivot):
    elAfterBorder = start

    for i in range(start, pivot):
        if tab[i] < tab[pivot]:
            tab[i], tab[elAfterBorder] = tab[elAfterBorder], tab[i]
            elAfterBorder += 1

    tab[pivot], tab[elAfterBorder] = tab[elAfterBorder], tab[pivot]
    return elAfterBorder

def quickSort(tab, start, end):
    while start < end:
        pivot = border(tab, start, end)
        quickSort(tab, start, pivot - 1)
        start = pivot + 1
    return tab

tab = [2, 4,6, 7,567,2, 43, 2,1]
quickSort(tab, 0, len(tab) - 1)
print(tab)