'''
Aleksandra Poskróbek

Idea algorytmu opiera się na podstawowym wyszukiwaniu dla każdego odcinka odcinków się w nim zawierających, jednak zawiera
ulepszenia znacznie poprawiające jego wydajność i czas pracy.
Na początek zastosowałam Qucik Sorta, w celu posortowania odcinków rosnąco po początku, a jeśli początki są równe,
malejąco po końcach. Następnie przy tak posortowanych odcinkach łatwo zauważyć, że każdy następny, jeżeli zawiera się
w jakimś odcinku go poprzedzającym (czyli dłuższym), nie będzie miał więcej zawartych odcinków niż ten przed nim.
Dlatego w algorytmie wprowadzona jest funkcja, która wywołuje się tylko dla odcinków nie będących w żadnych innych
odcinkach.
Algorytm (w optymistycznej i uśrednionej) ma złożoność nlogn, ze względu na użycie QuickSorta, gdyż samo późniejsze
znajdowanie największej ilości odcinków jest liniowe (dla przykładów, optymistycznie) lub nlogn (w przeciętnym przypadku).
W pesymistycznej opcji algorytm quick sort będzie miał złożoność n^2 i tak samo będzie z wprowadzonym przeze mnie algorytmem.
Taka sytuacja jest np. w przypadku, gdy żaden odcinek nie będzie zawierał żadnego innego odcinka.
'''

from zad2testy import runtests

def divisionBorder(start, pivot_id, tab):
    border_id = start

    for i in range(start, pivot_id):
        if tab[i][0] < tab[pivot_id][0] or (tab[i][0] == tab[pivot_id][0] and tab[i][1] > tab[pivot_id][1]):
            tab[border_id], tab[i] = tab[i], tab[border_id]
            border_id += 1

    tab[border_id], tab[pivot_id] = tab[pivot_id], tab[border_id]
    return border_id

def quickSort(tab, start, end):
    while start < end:
        border = divisionBorder(start, end, tab)
        quickSort(tab, start, border - 1)
        start = border + 1
    return tab

def maxDepth(L, id, n):
    max = 0
    next_max = -1
    element = L[id][1]
    for j in range(id + 1, n):
        if element >= L[j][1]:
            max += 1
        elif next_max == -1:
            next_max = maxDepth(L, j, n)
    if next_max > max: return next_max
    return max

def depth(L):
    n = len(L)
    quickSort(L, 0, n - 1)

    max = maxDepth(L, 0, n)

    return max
    pass

runtests( depth )