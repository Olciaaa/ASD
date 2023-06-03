from zad4testy import runtests
class maximumBuildings:
    def __init__(self):
        self.maximumCapacity = 0
        self.buildings = []

maxBuildings = maximumBuildings()

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

def func(T, idx, p, current_val, current_buildings, indexes, dynamic):
    n = len(T)
    if idx >= n:
        if current_val > maxBuildings.maximumCapacity:
            maxBuildings.maximumCapacity = current_val
            maxBuildings.buildings = []
            for i in range(len(current_buildings)):
                maxBuildings.buildings.append(indexes[current_buildings[i]])
        return maxBuildings.maximumCapacity

    #print(idx, " ", p)
    #print(dynamic)

    town_right = 0
    if len(current_buildings) > 0: town_right = T[current_buildings[len(current_buildings) - 1]][2]
    if T[idx][1] > town_right and p - T[idx][3] >= 0:
        dynamic[idx][p] = 1 + max(func(T, idx + 1, p - T[idx][3], current_val + val(T[idx]), current_buildings + [idx], indexes, dynamic), func(T, idx + 1, p, current_val, current_buildings, indexes, dynamic))
        return dynamic[idx][p]
    dynamic[idx][p] = 1 + func(T, idx + 1, p, current_val, current_buildings, indexes, dynamic)
    return dynamic[idx][p]

def select_buildings(T, p):
    n = len(T)
    #print(T)
    indexes = [i for i in range(n)]
    dynamic = [[-1 for _ in range(p + 1)] for _ in range(n)]

    quickSort(T, 0, n - 1, indexes)
    print(func(T, 0, p, 0, [], indexes, dynamic))
    print(dynamic)
    #print(maxBuildings.maximumCapacity)
    #print(T[len(T) - 1])
    return maxBuildings.buildings

#runtests( select_buildings )

#h, a, b, w
#max = 20
#val: [3, 12, 9, 2, 27]
T = [(3, 3, 4, 19), (3, 11, 17, 7), (4, 8, 15, 15), (3, 1, 7, 15), (4, 12, 17, 7), (3, 1, 7, 3), (4, 8, 9, 7), (3, 11, 18, 15), (4, 20, 31, 19), (3, 17, 26, 7)]
#3, 18, 28, 18, 20, 18, 4, 21, 44, 27

print(select_buildings(T, 20))

#print(select_buildings(T, 40))