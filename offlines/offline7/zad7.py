'''
Aleksandra Poskróbek

Algorytm działa na bazie rekurencji, w skrócie szuka on czy w grafie skierowanym jest cykl Hamiltona. Zaczynamy od dowolnego wierzchołka i dowolnej strony,
u mnie jest to 0 wierzchołek i 1 strona (bez straty ogólności :)). Następnie dla każdego wierzchołka, do którego możemy się udać z obecnie
rozważanego, sprawdzamy dalszą drogę rekurencyjnie i zapisujemy obecny wierzchołek jako ten już odwiedzony. Jeżeli dojdziemy do momentu, w
którym zamknie się nasz cykl Hamiltona to funkcja rekurencyjna zwraca wartość True i możemy z niej wyjść, w innym przypadku szukamy dalej.
Jeżeli nie ma żadnego możliwego cyklu to funkcja musi przejść po wszystkich opcjach, co powoduje, że rozważany problem jest NPtrudny.
'''
from zad7testy import runtests

tripPath = []
visitedCities = []
graph = []
startIdx = 0
startSideIn = 1
def droga( G ):
    global visitedCities, tripPath, graph
    graph = G
    visitedCities = [False for _ in range(len(G))]
    tripPath = [-1 for _ in range(len(G))]
    if isPossible(startSideIn, startIdx, 0):
        return tripPath
    return None

def possibleSide(cityIdx, idx):
    if idx in graph[cityIdx][1]: return 1
    if idx in graph[cityIdx][0]: return 0
    return None

def isPossible(sideIn, currentCityIdx, steps):
    sideOut = 0
    if sideIn == 0: sideOut = 1

    if steps == len(graph) - 1 and startIdx in graph[currentCityIdx][sideOut] and currentCityIdx in graph[startIdx][startSideIn]:
        tripPath[steps] = currentCityIdx
        return True
    if steps == len(graph) - 1:
        return False

    tripPath[steps] = currentCityIdx
    visitedCities[currentCityIdx] = True
    for cityIdx in graph[currentCityIdx][sideOut]:
        if not visitedCities[cityIdx]:
            sideInNewCity = possibleSide(cityIdx, currentCityIdx)
            if sideInNewCity is not None:
                if isPossible(sideInNewCity, cityIdx, steps + 1):
                    return True

    visitedCities[currentCityIdx] = False
    return False

runtests( droga, all_tests = True )