'''Szymon Woźniak
Mój program to dynamik. Zaczynamy od dwóch wywołań dla całego przedziału a,b, jednego z wejściem od zachodu, drugiego
z wejściem od wschodu. Koniec końców sprawdzimy, która z tych dwóch opcji będzie lepsza, poprzez wyliczenie maxa. W funkcji
dynamicznej mamy warunki końca. Jeżeli dzień jest równy długości, to znaczy, że nie ma już co zbierać, zwracamy 0. Jeżeli
a == b to jest to potencjalnie ostatni ruch więc jeżeli da się coś zwrócić, to to zwracamy, inaczej 0 (Dlatego max, żeby
nie robić w tym miejscu ifów). Następnie musimy rozważyć dla każdej z opcji (wjazd zachodem/wschodem) wszystkie przypadki
pośrednie. tj. jeżeli wjeżdżamy od zachodu, to funkcja zwróci wartość tego pola MINUS dni, które już zostały "stracone"
DODAĆ wywolanie funkcji dla następnego pola z jednej, a potem z drugiej strony (wybierzemy lepsze). analogicznie robimy 
w przypadku wjazdach od strony wschodniej, tylko wtedy "wskaznik" przesuwa się w lewo. Dla każdego z takich "4" przypadków
liczymy jego lokalne maxima, a następnie obliczamy jedno globalne maximum z wszystkich tych 4 opcji. Dodajemy w rekurencji
spamiętywanie i tworzy się nam funkcja dynamiczna. Złożoność mojego programu - pamięciowa wynosi O(n^3) i dodatkowo w funkcji
rekurencyjnej wykonujemy O(n) operacji, więc koniec konców złożoność czasowa wynosi O(n^4)
'''


from egz1atesty import runtests

def f(DP, S, a, b, wz, d): 
    #print(a, b, wz, d)
    if d == len(S):
        return 0 

    if DP[a][b][d][wz] is not None:
        return DP[a][b][d][wz]

    if a == b:
        return max(0, S[a]-d)
    
    #a, b - przedział. wz - wschód 0 /zachód 1. d - dzień. (start 0 max len(S)-1)
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    if wz == 1:
        for i in range(a, b+1):
            w1 = max(w1, max(0, S[i]-d) + f(DP, S, i+1, b, 0, d+1))
            w2 = max(w2, max(0, S[i]-d) + f(DP, S, i+1, b, 1, d+1))
    if wz == 0:
        for i in range(a, b+1):
            w3 = max(w3, max(0, S[i]-d) + f(DP, S, a, i-1, 0, d+1))
            w4 = max(w4, max(0, S[i]-d) + f(DP, S, a, i-1, 1, d+1))
    
    DP[a][b][d][wz] = max(0, w1, w2, w3, w4)
    return DP[a][b][d][wz]
    


def snow( S ):
    # tu prosze wpisac wlasna implementacje
    #DP[a][b][d][wz]
    n = len(S)
    DP = [[[[None for _ in range(2)] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
    res1 = f(DP, S, 0, len(S)-1, 0, 0)
    res2 = f(DP, S, 0, len(S)-1, 1, 0)
    return max(res1, res2)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )