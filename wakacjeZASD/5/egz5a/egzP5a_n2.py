from egzP5atesty import runtests 

def inwestor ( T ):
    T = [-1] + T + [-1] #o(n)

    maximum = 0
    for i in range(1, len(T) - 1):
        maximum = max(countWhenISmallest(T, i), maximum)
    #tutaj proszę wpisać własną implementację 
    return maximum

def countWhenISmallest(T, i):
    left = 0
    right = 0
    idx = i

    while T[idx] >= T[i]:
        idx -= 1
    left = idx

    idx = i
    while T[idx] >= T[i]:
        idx += 1
    right = idx

    return (right - left - 1) * T[i]

runtests ( inwestor, all_tests=True )