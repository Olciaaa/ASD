from egzP7btesty import runtests

def ogrod( S, V ):
    maximum = 0
    originalS = []
    for el in S:
        originalS.append(el)
    currMax, types = maximumGain(S, V, 0)

    for i in range(len(S)):
        S[i] = (S[i], i)
    S.sort(key = lambda x: x[0])


    nextIdxOfType = [-1 for _ in range(len(V))]

    for i in range(len(S)):
        if nextIdxOfType[S[i][0] - 1] == -1:
            nextIdxOfType[S[i][0] - 1] = i
    print(nextIdxOfType)
    maximumForStart = [0 for _ in range(len(S))]
    maximum = currMax[len(currMax) - 1]
    change = 0
    maximumForStart[0] = maximum

    for i in range(0, len(S)):
        type_idx = originalS[i] - 1
        types[type_idx] -= 1

        nextIdxOfType[type_idx] += 1

        if types[type_idx] == 0:
            maximumForStart[i] = maximum - V[type_idx]
            maximum -= V[type_idx]
            change -= V[type_idx]
        elif types[type_idx] == 1:
            maximumForStart[i] = maximum + V[type_idx]
            maximum += V[type_idx]
            change += V[type_idx]

        else:
            if S[nextIdxOfType[type_idx]][0] - 1 == type_idx:
                a = S[nextIdxOfType[type_idx]][1]
                print(a)
                maximum = max(maximum, currMax[a] + change)
                maximumForStart[i] = maximum


    print(maximumForStart)
    #Tutaj proszę wpisać własną implementację
    return maximum

def maximumGain(S, V, idx):
    types = [0 for _ in range(len(V))]
    types[S[idx] - 1] += 1
    currMax = [0 for _ in range(len(S))]
    currMax[idx] = V[S[idx] - 1]
    maximum = V[S[idx] - 1]
    curr = maximum

    for i in range(idx + 1, len(S)):
        types[S[i] - 1] += 1
        if types[S[i] - 1] == 1: curr += V[S[i] - 1]
        elif types[S[i] - 1] == 2: curr -= V[S[i] - 1]
        maximum = max(maximum, curr)
        currMax[i] = curr

    return currMax, types
runtests(ogrod, all_tests = True)