'''
Zadanie 2. (najdłuższy wspólny podciąg) Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć długość
ich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamiczny O(n2)).
'''

def ex2(A, B):
    max = 0
    for i in range(len(A)):
        if maximum_length(A, B, i, i):
            print("haha")

    return

def maximum_length(A, B, id_A, id_B):
    return