from zad1testy import runtests

Data = []
dynamic = []
def intuse( I, x, y ):
    global Data, dynamic
    dynamic = [-1 for _ in range(len(I))]
    Data = I

    for i in range(len(Data)):
        Data[i] = (Data[i][0], Data[i][1], i)

    I.sort(key = lambda x: (x[0], x[1]))

    idx = 0
    while Data[idx][0] <= x:
        if Data[idx][0] == x: rec(idx, y)
        idx += 1
    #print(dynamic)
    print(len(I))
    results = []
    for i in range(len(dynamic)):
        if dynamic[i] == True:
            results.append(Data[i][2])

    return results

def rec(idx, y):
    global Data, dynamic
    if Data[idx][1] == y:
        dynamic[idx] = True
        return True
    if Data[idx][1] > y:
        dynamic[idx] = False
        return False
    if idx >= len(Data):
        dynamic[idx] = False
        return False

    if dynamic[idx] != -1:
        return dynamic[idx]

    flag = False
    for i in range(idx + 1, len(Data)):
        if Data[i][0] == Data[idx][1]:
            if rec(i, y):
                flag = True
        if Data[i][0] > Data[idx][1]: break

    dynamic[idx] = flag
    return dynamic[idx]


I = [(3,4), (2,5), (1,3), (4,6), (1,4)]
x = 1
y = 6
intuse(I, x, y)
runtests( intuse )


