from egzP7btesty import runtests

def ogrod( S, V ):
    maximum = 0
    for i in range(len(S)):
        maximum = max(maximum, maximumGain(S, V, i))
    #Tutaj proszę wpisać własną implementację
    return maximum

def maximumGain(S, V, idx):
    types = [0 for _ in range(len(V))]
    types[S[idx] - 1] += 1
    maximum = V[S[idx] - 1]
    curr = maximum

    for i in range(idx + 1, len(S)):
        types[S[i] - 1] += 1
        if types[S[i] - 1] == 1: curr += V[S[i] - 1]
        elif types[S[i] - 1] == 2: curr -= V[S[i] - 1]
        maximum = max(maximum, curr)

    return maximum
runtests(ogrod, all_tests = True)