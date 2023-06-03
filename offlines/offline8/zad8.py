from zad8testy import runtests

def highway( A ):
    print(listOfLengths(A))
    return None

def listOfLengths(A):
    tab = []

    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            length = ((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** 0,5
            tab.append((length, i, j))
    tab.sort(key=lambda x: (x[0]))

    return tab

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = False )