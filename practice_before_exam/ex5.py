'''
Zadanie 5. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
znajdujący trasę o minimalnym koszcie.
'''

def zad5(tab):
    n = len(tab)
    dynamic = [[-1 for _ in range(n)]for _ in range(n)]

    val = recursive(tab, dynamic, 0, 0)

    for el in dynamic:
        print(el)

    x = n - 1
    y = n - 1
    toReturn = []
    while not (x == y == 0):
        toReturn.append((x, y))
        if x == 0: y = y - 1
        elif y == 0: x = x - 1
        else:
            if dynamic[y - 1][x] > dynamic[y][x - 1]:
                x = x - 1
            else: y = y - 1
    toReturn.append((0, 0))


    return toReturn[::-1]

def recursive(tab, dynamic, curr_x, curr_y):
    n = len(tab)

    if curr_x == curr_y == n - 1:
        return tab[n - 1][n - 1]

    if dynamic[curr_y][curr_x] != -1:
        return dynamic[curr_y][curr_x]

    if curr_x == n - 1:
        dynamic[curr_y][curr_x] = recursive(tab, dynamic, curr_x, curr_y + 1) + tab[curr_y][curr_x]
        return dynamic[curr_y][curr_x]
    elif curr_y == n - 1:
        dynamic[curr_y][curr_x] = recursive(tab, dynamic, curr_x + 1, curr_y) + tab[curr_y][curr_x]
        return dynamic[curr_y][curr_x]

    '''if curr_x == n - 1:
        value = 0
        for i in range(curr_y + 1, n):
            value += tab[i][curr_x]
        return value'''

    dynamic[curr_y][curr_x] = min(recursive(tab, dynamic, curr_x, curr_y + 1), recursive(tab, dynamic, curr_x + 1, curr_y)) + tab[curr_y][curr_x]
    return dynamic[curr_y][curr_x]


A = [[1,3,5,7,3],
     [1,1,1,2,2],
     [2,4,1,8,3],
     [1,2,1,1,1],
     [1,3,5,6,1]]

print(zad5(A))