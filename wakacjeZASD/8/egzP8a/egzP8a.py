from egzP8atesty import runtests 

def reklamy ( T, S, o ):
    #print(T)
    #print(S)
    #print(o)
    for i in range(len(T)):
        T[i] = [T[i], S[i]]
    T.sort()
    #Tutaj proszę wpisać własną implementację 
    return maximumIncome(T, o)

def maximumIncome(T, limit):
    maximum = 0
    for idx in range(len(T)):
        if T[idx][0][1] > limit:
            break

        curr = T[idx][1]
        for j in range(idx + 1, len(T)):
            if T[j][0][1] > limit:
                break

            if T[j][0][0] > T[idx][0][1]:
                curr = max(curr, T[idx][1] + T[j][1])
        maximum = max(curr, maximum)
    return maximum

runtests ( reklamy, all_tests=True )