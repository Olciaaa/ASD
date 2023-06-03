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

    if steps == len(graph) and currentCityIdx == startIdx:
        return True

    if visitedCities[currentCityIdx]: return False

    tripPath[steps] = currentCityIdx
    visitedCities[currentCityIdx] = True
    for cityIdx in graph[currentCityIdx][sideOut]:
        sideInNewCity = possibleSide(cityIdx, currentCityIdx)
        if sideInNewCity is not None:
            if isPossible(sideInNewCity, cityIdx, steps + 1):
                return True

    visitedCities[currentCityIdx] = False
    return False

runtests( droga, all_tests = True )