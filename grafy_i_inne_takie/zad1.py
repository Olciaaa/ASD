'''
Mamy dany nieskierowany graf G = (V, E).
Dla każdego wierzchołka v należy wybrać liczbę naturalną f(v) (nazywaną kolorem v) tak, żeby dla każdej
krawędzi {x, y} ∈ E zachodzilo, ze f(x) != f(y). Należy użyć jak najmniej kolorów (czyli zbior f(V ) powinien
mieć minimalną liczność). Problem jest NP-zupełny więc nie istnieje optymalny algorytm wielomianowy (o
ile P jest różne od NP). Proszę podać algorytm zachłanny, który używa najwyżej D + 1 kolorów, gdzie D to
maksymalny stopień wierzchołka w G.
'''

def colouring(G):
    colors = []
