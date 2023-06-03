from kol2atesty import runtests
Points = []
e = 0
dynamic = []

def drivers( P, B ):
    global Points, e, dynamic
    Points = P
    for i in range(len(Points)):
        Points[i] = (Points[i][0], Points[i][1], i)
    e = B
    dynamic = [[[-1 for _ in range(len(P))] for _ in range(2)]for _ in range(4)]
    Points.sort()
    # tu prosze wpisac wlasna implementacje
    print(rec(0, 0, 2))
    #for el in dynamic:
        #print(el)

    results =[]

    idx = 0
    who = 0
    k = 2

    while idx < len(Points):
        if Points[idx][1]:
            if k == 0:
                results.append(Points[idx][2])
                who = (who + 1) % 2
                k = 2
            else:
                min_who = who
                min_k = k - 1
                if idx + 1 < len(Points) and (dynamic[k][(who + 1) % 2][idx + 1] < dynamic[min_k][min_who][idx + 1]):
                    min_who = (who + 1) % 2
                    min_k = 2
                    results.append(Points[idx][2])
                who = min_who
                k = min_k

        idx += 1
    print(results)
    return results

def rec(idx, who, numOfPoints):
    if idx == len(Points):
        return 0

    if dynamic[numOfPoints][who][idx] != -1:
        return dynamic[numOfPoints][who][idx]

    if Points[idx][1]:
        if numOfPoints == 0:
            dynamic[numOfPoints][who][idx] = rec(idx + 1, (who + 1) % 2, 2)
            return dynamic[numOfPoints][who][idx]

        dynamic[numOfPoints][who][idx] = min(rec(idx + 1, (who + 1) % 2, 2), rec(idx + 1, who, numOfPoints - 1))
        return dynamic[numOfPoints][who][idx]

    dynamic[numOfPoints][who][idx] = rec(idx + 1, who, numOfPoints) + who
    return dynamic[numOfPoints][who][idx]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )