'''
Otrzymujemy na wejściu listę par ludzi, które się wzajemnie znają. Osoby są reprezentowane przez liczby od 0 do n - 1.

Dnia pierwszego osoba 0 przekazuje pewną wiadomość wszystkim swoim znajomym. Dnia drugiego każdy ze znajomych przekazuje
 tę wiadomość wszystkim swoim znajomym, którzy jej jeszcze nie znali, i tak dalej.

Napisz algorytm, który zwróci dzień, w którym najwięcej osób poznało wiadomość oraz ilość osób, które tego dnia ją otrzymały.
'''
from queue import Queue


def theDay(friends, s):
    visited = [False for _ in range(len(friends))]
    distanceFromS = [0 for _ in range(len(friends))]
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        s = q.get()

        for i in range(len(friends[s])):
            if not visited[friends[s][i]]:
                q.put(friends[s][i])
                visited[friends[s][i]] = True
                distanceFromS[friends[s][i]] = distanceFromS[s] + 1

    results = [0 for _ in range(len(friends))]
    for dist in distanceFromS:
        results[dist] += 1

    idx_max = 0
    maximum = results[0]

    for i in range(len(results)):
        if results[i] > maximum:
            idx_max = i
            maximum = results[i]

    return idx_max, maximum
G1 = [[1], [0, 2, 4, 5], [1, 3], [2], [1, 5], [1, 4]]
print(theDay(G1, 0))