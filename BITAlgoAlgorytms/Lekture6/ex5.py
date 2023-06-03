'''
Dostałeś sejf, który odblokowuje się czterocyfrowym PINem (0000 - 9999). Pod wyświetlaczem znajduje się kilka przycisków
z liczbami od 1 do 9999 - przykładowo (13, 223, 782, 3902). Sejf ten działa inaczej niż normalny: wciśnięcie przycisku z
liczbą powoduje dodanie liczby z przycisku do liczby na wyświetlaczu. Jeżeli suma jest większa niż 9999, to pierwsza
cyfra zostaje obcięta.

Jest tobie znany PIN oraz cyfry, które są aktualnie wyświetlane. Znajdź najkrótszą sekwencję naciśnięć przycisków, która
pozwoli ci odblokować sejf. Jeżeli taka sekwencja nie istnieje, zwróć None.
'''
from queue import Queue

def bestSequence(numbers, pin):
    G = [[] for _ in range(10000)]

    for i in range(10000):
        for j in numbers:
            G[i].append((i + j) % 10000)

    return bfs(G, 0, pin)

def bfs(G, s, e):
    visited = [False for _ in range(len(G))]
    distanceFromS = [0 for _ in range(len(G))]
    parents = [-1 for _ in range(len(G))]
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        s = q.get()

        if s == e: return distanceFromS[s]

        for i in range(len(G[s])):
            if not visited[G[s][i]]:
                parents[G[s][i]] = s
                q.put(G[s][i])
                visited[G[s][i]] = True
                distanceFromS[G[s][i]] = distanceFromS[s] + 1
    return None

print(bestSequence([13, 223, 782, 3902], 9394))
