from zad4testy import runtests

def select_buildings(T,p):
    dynamic = [[-1 for _ in range(p + 1)] for _ in range(len(T))]
    for i in range(len(T)):
        T[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    T.sort(key=lambda x: (x[2], x[1]))
    maximum = 0
    for i in range(len(T)):
        value = recursive(T, dynamic, i, p)
        if value > maximum:
            maximum = value

    idx = p
    results = []
    for i in range(len(T)):
        if dynamic[i][idx] == maximum:
            results.append(T[i][4])
            maximum -= T[i][0] * (T[i][2] - T[i][1])
            idx -= T[i][3]

    return results

def recursive(T, dynamic, idx, left_p):
    if idx == len(T):
        return 0
    if left_p - T[idx][3] < 0:
        return 0

    maximum = 0
    rightSideOfCity = T[idx][2]

    if dynamic[idx][left_p] != -1:
        return dynamic[idx][left_p]

    for i in range(idx + 1, len(T)):
        if rightSideOfCity < T[i][1]:
            value = recursive(T, dynamic, i, left_p - T[idx][3])
            if value > maximum:
                maximum = value
    dynamic[idx][left_p] = maximum + T[idx][0] * (T[idx][2] - T[idx][1])
    return maximum + T[idx][0] * (T[idx][2] - T[idx][1])


runtests( select_buildings )