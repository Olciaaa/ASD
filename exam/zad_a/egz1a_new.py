from egz1atesty import runtests
Data = []
dynamic = []
def snow( S ):
    global Data, dynamic
    # tu prosze wpisac wlasna implementacje
    Data = S
    dynamic = [[[[-1 for _ in range(len(S) + 1)]for _ in range(len(S) + 1)]for _ in range(len(S) + 1)]for _ in range(len(S) + 1)]
    return (rec(0, 0, len(S), 0))

def rec(idx, start, end, day):
    global Data, dynamic

    if idx == len(Data):
        dynamic[idx][start][end][day] = 0
        return 0
    if idx >= end:
        dynamic[idx][start][end][day] = 0
        return 0
    if idx < start:
        dynamic[idx][start][end][day] = 0
        return 0

    if dynamic[idx][start][end][day] != -1:
        return dynamic[idx][start][end][day]

    maximum = max(rec(idx + 1, start, end, day),
                  rec(idx + 1, idx + 1, end, day + 1) + Data[idx] - day,
                  rec(idx + 1, start, idx + 1, day + 1) + Data[idx] - day)
    dynamic[idx][start][end][day] = maximum
    return maximum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
snow([1, 7, 3, 4, 1])