from egz1atesty import runtests
Data = []
dynamic = []
dynamic2 = []
def snow( S ):
    global Data, dynamic, dynamic2
    Data = S
    dynamic = [[-1 for _ in range(len(S))] for _ in range(3)]
    dynamic2 = [[[] for _ in range(len(S))]for _ in range(3)]

    # tu prosze wpisac wlasna implementacje
    maximum = 0
    for i in range(len(Data)):
        one = rec(i, Data, 1)
        two = rec(i, Data, 0)

        maximum = max(maximum, one, two)

    return maximum

def rec(idx, actualData, side):
    global dynamic, dynamic2
    maximum = 0
    actual = [0 for _ in range(len(actualData))]
    snow = actualData[idx]
    #true - z lewa
    #false - z prawa
    end = True
    for i in range(len(actualData)):
        if actualData[i] > 0:
            end = False

    if end or idx == len(actualData):
        for i in range(len(actualData)):
            dynamic2[side][idx].append(actualData[i])
        dynamic[side][idx] = 0
        return 0

    flag = True
    start = 0
    end = idx + 1
    if side == 1:
        start = idx
        end = len(actualData)
    for i in range(start, end):
        #print(dynamic2)
        if len(dynamic2[side][idx]) == 0:
            flag = False
            break
        if dynamic2[side][idx][i] != actualData[i]: flag = False
    if flag and dynamic[side][idx] != -1:
        print("haha")
        return dynamic[side][idx]

    for i in range(len(actualData)):
        actual[i] = actualData[i] - 1
    if side == 1:
        for i in range(idx + 1):
            actual[i] = 0
    if side == 0:
        for i in range(idx, len(actualData)):
            actual[i] = 0

    for i in range(idx + 1, len(Data)):
        one = rec(i, actual, 1)
        two = rec(i, actual, 0)

        maximum = max(maximum, one, two)
    for i in range(len(actualData)):
        dynamic2[side][idx].append(actualData[i])
    dynamic[side][idx] = maximum + snow
    return maximum + snow
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
S = [1, 7, 3, 4, 1]
print(snow(S))