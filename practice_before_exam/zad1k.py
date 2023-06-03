'''
Zadanie 1 - Największa różnica w podciągu
Szablon rozwiązania: zad1k.py
Dany jest ciąg binarny tj. zer oraz jedynek S. Proszę znaleźć taki SPÓJNY fragment tego
ciągu, w którym różnica pomiędzy ilością zer, a jedynek, będzie jak największa. Jeżeli w
ciągu występują same jedynki, należy założyć, że rozwiązaniem jest -1
Algorytm należy zaimplementować jako funkcję postaci:
def roznica( S ):
...
która przyjmuje ciąg S i zwraca wyliczoną największą osiągalną różnicę.
Przykład. Dla ciągu:
11000010001
Wynikiem jest liczba 6
Testowanie Rozwiązań
Żeby przetestować rozwiązania należy wykonać polecenie: python3 zad1k.py
'''

from zad1ktesty import runtests

def roznica( S ):
    return difference(S)

def difference(S):
    max_difference = -1
    for start in range(len(S)):
        diff = -1
        if S[start] == '0':
            diff = 1
        for end in range(start + 1, len(S)):
            if S[end] == '0':
                diff += 1
            else: diff -= 1

            if diff > max_difference:
                max_difference = diff
    return max_difference





runtests ( roznica )