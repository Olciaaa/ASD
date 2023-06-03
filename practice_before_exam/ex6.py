'''
Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T.
Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).
'''

def zad6(values_of_money, money_to_get):
    dynamic = [[-1 for _ in range(money_to_get + 1)] for _ in range(len(values_of_money))]

    minimum = float('inf')
    for i in range(len(values_of_money)):
        next_coin_value = recursive(values_of_money, dynamic, i, money_to_get)
        if next_coin_value < minimum:
            minimum = next_coin_value
    for el in dynamic:
        print(el)

    return minimum

def recursive(tab, dynamic, idx, current_amount):
    if current_amount == 0:
        return 0

    if dynamic[idx][current_amount] != -1:
        return dynamic[idx][current_amount]

    minimum = float('inf')
    for i in range(len(tab)):
        if current_amount - tab[idx] >= 0:
            next_coin_value = recursive(tab, dynamic, i, current_amount - tab[idx])
            if next_coin_value < minimum:
                minimum = next_coin_value
    dynamic[idx][current_amount] = minimum + 1
    return minimum + 1

A = [1,5,8]
print(zad6(A, 25))