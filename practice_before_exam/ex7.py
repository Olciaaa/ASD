'''
Problem plecakowy często przedstawia się jako problem złodzieja rabującego sklep – znalazł on N towarów; j-ty przedmiot
jest wart cj oraz waży wj Złodziej dąży
do zabrania ze sobą jak najwartościowszego łupu, przy czym nie może zabrać więcej niż B kilogramów. Nie może też zabierać
ułamkowej części przedmiotów (byłoby to możliwe w ciągłym problemie plecakowym).

Proszę zaimplementować rozwiązanie problemu plecakowego przy pomocy rekurencji ze spamiętywaniem.

Proszę zaimplementować rozwiązanie problemu plecakowego tak, żeby funkcja
zwracały listę indeksów przedmiotów, które należy wybrać (można korzystać z
funkcji append do dopisywania elementów na końcu listy)
'''

def zad7(gooddies, capacity):
    dynamic = [[-1 for _ in range(capacity + 1)] for _ in range(len(gooddies))]
    maximum = 0
    for gooddie_idx in range(0, len(gooddies)):
        value = recursive(dynamic, gooddies, gooddie_idx, capacity)
        if value > maximum:
            maximum = value

    for el in dynamic:
        print(el)

    idx = capacity
    result = []
    for gooddie_idx in range(len(gooddies)):
        if dynamic[gooddie_idx][idx] == maximum:
            result.append(gooddie_idx)
            idx -= gooddies[gooddie_idx][0]
            maximum -= gooddies[gooddie_idx][1]

    return result

def recursive(dynamic, goddies, idx, capacity_left):
    if idx == len(goddies):
        return 0

    if capacity_left - goddies[idx][0] < 0:
        return 0

    if dynamic[idx][capacity_left] != -1:
        return dynamic[idx][capacity_left]

    maximum_val = 0
    for i in range(idx + 1, len(goddies)):
        val = recursive(dynamic, goddies, i, capacity_left - goddies[idx][0])
        if val > maximum_val:
            maximum_val = val
    dynamic[idx][capacity_left] = maximum_val + goddies[idx][1]
    return maximum_val + goddies[idx][1]

#[waga, wartość]
tab = [[3,4],
       [2,4],
       [1,4],
       [4,6]]
B = 3
print(zad7(tab, B))

tab = [
    [10,1],
    [3,5],
    [3,5],
    [3,2],
    [2,6],
    [6,8],
    [8,2],
    [7,9],
    [6,3]
]

B = 8
print(zad7(tab, B))
