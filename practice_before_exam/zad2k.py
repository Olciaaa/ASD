'''
Zadanie 2 - Najdłuższy palindrom
Szablon rozwiązania: zad2k.py
Dany jest ciąg liter S. Proszę znaleźć taki SPÓJNY fragment tego podciągu, który będzie
najdłuższym możliwym palindromem.
Algorytm należy zaimplementować jako funkcję postaci:
def palindrom( S ):
...
która przyjmuje ciąg S i zwraca ten najdłuższy palindrom.
Przykład. Dla ciągu:
aacaccabcc
Wynikiem jest ciąg acca
Testowanie Rozwiązań
Żeby przetestować rozwiązania należy wykonać polecenie: python3 zad2k.py
'''

from zad2ktesty import runtests

def palindrom(S):
    print(S)
    dynamic = [[-1 for _ in range(len(S))]for _ in range(len(S))]

    for i in range(len(S)):
        for j in range(i, len(S)):
            if dynamic[i][j] != -1: return dynamic[i][j]
            if(isPalindrome(S, i, j)):
                dynamic[i][j] = j - i + 1

    #for el in dynamic:
        #print(el)

    #Tutaj proszę wpisać własną implementację
    return ""

def isPalindrome(S, idx1, idx2):
    if idx1 == idx2:
        return True

    if idx2 - idx1 == 1:
        if S[idx1] == S[idx2]:
            return True
        else:
            return False

    if(S[idx1] == S[idx2]):
        return isPalindrome(S, idx1 + 1, idx2 - 1)
    return False

palindrom("cabba")
runtests(palindrom)
