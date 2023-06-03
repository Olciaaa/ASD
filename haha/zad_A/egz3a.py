from egz3atesty import runtests

# Zauważmy, że wystarczy sprawdzać czy powstaje nowy śnieg
# czy on się kończy. Możemy wrzucić wszystko do jednej tablicy,
# jeżeli w tym miejscu zaczyna się śnieg, to dodajemy do naszego
# licznika +1, jeżeli w tym miejscu kończy się śnieg, to nasz
# wynik końcowy to max(wynik końcowy, licznik) i odejmujemy
# od naszego licznika -1. Do utworzenia jednej tablicy dodajemy
# wszystkie elementy z tablicy I jako krotki (el, 0) jeżeli
# śnieg się zaczyna, albo jako krotki (el, 1) jeżeli śnieg się kończy.
# Sortowanie jednej tablicy to O(nlog(n)), a potem przejście po niej
# to O(n), złożoność to O(nlog(n)).

def snow(T, I):
    output = 0
    X = []
    for el in I:
        X.append((el[0], 0))
        X.append((el[1], 1))

    X.sort()
    temp = 0
    for el in X:
        if el[1] == 0:
            output = max(temp, output)
            temp += 1
        else:
            output = max(temp, output)
            temp -= 1

    return output


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)




