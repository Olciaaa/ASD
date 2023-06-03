'''
Zadanie 1. (problem sumy podzbioru) Dana jest tablica n liczb A. Proszę podać i zaimplementować
algorytm, który sprawdza, czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T.
'''

def ex1(A, T):
    for i in range(len(A)):
        if is_possible(A, T, i, A[i]): return True

    return False

def is_possible(tab, to_find, idx, curr_val):
    if curr_val == to_find: return True
    elif curr_val > to_find: return False

    if idx == len(tab):
        return False

    for i in range(idx + 1, len(tab)):
        if is_possible(tab, to_find, i, curr_val + tab[i]): return True

    return False

tab = [6,8,4,4,2, 8,10,6]
T = 29

print(ex1(tab, T))











'''def ex1(A, T):
    dynamic = [[0 for _ in range(T)] for _ in range(len(A))]
    for i in range(T):
        dynamic[0][i] = A[0]
    for i in range(1, len(A)):
        dynamic[i][0] = A[i]
        if sumOfElements(A, i, A[i], T, dynamic):
            return True

    return False

def sumOfElements(A, idx, current_val, T, dynamic):
    if current_val == T: return True

    if current_val > T: return False

    if idx == len(A):
        return False

    val = False
    dynamic[idx][current_val] = dynamic[idx - 1][current_val]
    for i in range(idx + 1, len(A)):
        if sumOfElements(A, i, current_val + A[i], T, dynamic): val = True

    return val


tab = [6,8,4,4,2,5,6,7]
T = 15

print(ex1(tab, T))'''