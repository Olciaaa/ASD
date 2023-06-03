from zad7testy import runtests

def droga( G ):
    tab = [False for _ in range(len(G))]

    return isPossible(G, 0, 1, 1, 0, tab, [])

def possibleSide(G, cityIdx, idx):
    if idx in G[cityIdx][1]: return 1
    if idx in G[cityIdx][0]: return 0
    return None

def isPossible(G, startIdx, startSideIn, sideIn, currentCityIdx, visitedCities, tripPath):
    sideOut = 0
    if sideIn == 0: sideOut = 1

    if len(tripPath) == len(G) - 1 and startIdx in G[currentCityIdx][sideOut] and currentCityIdx in G[startIdx][startSideIn]:
        return tripPath + [currentCityIdx]
    if len(tripPath) == len(G) - 1: return None

    visitedCities[currentCityIdx] = True
    for cityIdx in G[currentCityIdx][sideOut]:
        if not visitedCities[cityIdx]:
            sideInNewCity = possibleSide(G, cityIdx, currentCityIdx)
            if sideInNewCity is not None:
                flag = isPossible(G, startIdx, startSideIn, sideInNewCity, cityIdx, visitedCities, tripPath + [currentCityIdx])
                if flag is not None: return flag

    visitedCities[currentCityIdx] = False
    return None

runtests( droga, all_tests = True )