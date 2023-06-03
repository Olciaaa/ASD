'''
Aleksandra Poskróbek
Mój pomysł opiera się w znaczącej mierze na zachowaniu i właściwościach kolejki priorytetowej. Idę po elementach tablicy,
dopóki nie zbiorę ropy wystarczającej na przejście od punktu 0 do n - 1.

Kiedy dochodzę do indeksu, gdzie nie mogłabym dalej iść z dotychczasową ropą, to wyciągam pierwszy element z kolejki,
który jest jednocześnie największą możliwą plamą i dodaję otrzymaną ropę do zebranej ropy, a indeks do tablicy z wynikami.
Następnie idę dalej i dodaję do kolejki priorytetowej kolejne możliwe elementy. I tak w kółko, aż do otrzymania ropy, która
pozwala dojechać z miasta A do B.
Problem z sortowaniemm domyślnym listy (sortowanie jest rosnące, a potrzebuję malejące) rozwiązałam poprzez zamianę znaku
wielkości plamy przy dodawaniu do kolejki.

Złożonosc czasowa to O(nlogn)
'''

from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    fields_in_order = PriorityQueue()
    stops = [0]
    n = len(T)
    oilGained = T[0]
    idx = 1
    while n - 1 > oilGained:
        fields_in_order.put((-T[idx], idx))

        if idx == oilGained:
            currently_biggest_oil = fields_in_order.get()
            stops.append(currently_biggest_oil[1])
            oilGained -= currently_biggest_oil[0]
        idx += 1
    stops.sort()
    return stops

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )