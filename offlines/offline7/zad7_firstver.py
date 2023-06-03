from zad7testy import runtests

def droga( G ):
    for i in range(len(G)):
        tab = isPossible(G, i, 1, 1, i, [])

        if tab is not None:
            return tab
        tab = isPossible(G, i, 0, 0, i, [])
        if tab is not None:
            return tab

    return None

def possibleSide(G, cityIdx, idx):
    if idx in G[cityIdx][1]: return 1
    if idx in G[cityIdx][0]: return 0
    return None

def isPossible(G, startIdx, startSideIn, sideIn, idx, vertices):
    sideOut = 0
    if sideIn == 0: sideOut = 1

    if  len(vertices) == len(G) - 1 and startIdx in G[idx][sideOut] and idx in G[startIdx][startSideIn]:
        return vertices + [idx]

    for cityIdx in G[idx][sideOut]:
        sideInNewCity = possibleSide(G, cityIdx, idx)
        if sideInNewCity is not None and cityIdx not in vertices:
            flag = isPossible(G, startIdx, startSideIn, sideInNewCity, cityIdx, vertices + [idx])
            if flag is not None: return flag

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )