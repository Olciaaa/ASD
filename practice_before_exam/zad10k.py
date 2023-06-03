from zad10ktesty import runtests

def dywany ( N ):
    #print(N)

    dynamic = [[-1 for _ in range(N + 1)] for _ in range(int(N ** (1 / 2)) + 1)]

    minimum = N
    for i in range(int(N ** (1 / 2)), int(N ** (1 / 2))//2, -1):
        value = recursive(dynamic, i, N)
        if value < minimum:
            minimum = value

    ls = N
    toReturn = []
    while not ls == 0:
        minimum = ls
        idx_min = int(ls ** (1 / 2))
        for i in range(int(ls ** (1 / 2)), int(ls ** (1 / 2)) // 2, -1):
            value = dynamic[i][ls]
            if value < minimum:
                minimum = value
                idx_min = i
        ls -= idx_min ** 2
        toReturn.append(idx_min)

    return toReturn

def recursive(dynamic, size_of_carpet, left_space):
    if left_space == 0:
        return 0

    if dynamic[size_of_carpet][left_space] != -1:
        return dynamic[size_of_carpet][left_space]

    left_space -= size_of_carpet ** 2

    minimum = left_space
    for i in range(int(left_space ** (1/2)), int(left_space ** (1/2))//2, -1):
        value = recursive(dynamic, i, left_space)
        if value < minimum:
            minimum = value
    dynamic[size_of_carpet][left_space + size_of_carpet ** 2] = minimum + 1
    return minimum + 1


runtests( dywany )

