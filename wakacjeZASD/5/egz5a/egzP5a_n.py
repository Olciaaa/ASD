from egzP5atesty import runtests


def inwestor(T):
    T = [-1] + T + [-1]  # o(n)

    for i in range(len(T)):
        T[i] = [-1, -1, T[i]]

    countLeftsAndRights(T)
    maximum = 0

    for i in range(1, len(T) - 1):
        maximum = max(maximum, (T[i][1] - T[i][0] - 1) * T[i][2])
    # tutaj proszę wpisać własną implementację
    return maximum


def countLeftsAndRights(T):
    stos = [0]

    for i in range(1, len(T)):
        if T[i][2] > T[stos[-1]][2]:
            T[i][0] = stos[-1]
        else:
            while len(stos) > 0 and T[stos[-1]][2] >= T[i][2]:
                T[stos.pop()][1] = i
            if len(stos) > 0: T[i][0] = stos[-1]
        stos.append(i)
   # print(T)


runtests(inwestor, all_tests=True)
