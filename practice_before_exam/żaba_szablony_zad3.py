from żaba_zad3testy import runtests

def iamlate(T, V, q, l):
    dynamic = [[-1 for _ in range(q + 1)] for _ in range(len(T))]
    print(recursive(dynamic, T, V, l, q, 0, 0))

    max_q = q
    i = 0
    q = 0
    result = []
    while not (T[i] + q >= l or i == len(T) - 1):
        result.append(i)
        q = min(V[i] + q, max_q)
        idx = i + 1
        minimum = float('inf')
        idx_min = i + 1
        while idx < len(T) and T[idx] <= q + T[i]:
            val = dynamic[idx][q - T[idx] + T[i]]
            #print(val)
            if val < minimum and val != -1:
                minimum = val
                idx_min = idx
            idx += 1
        q = q - T[idx_min] + T[i]
        i = idx_min


    if T[i] + q >= l:
        return result

    if i == len(T) - 1:
        if min(q + V[i], max_q) + T[i] >= l:
            result.append(i)
            return result
        else:
            return []

    return result

def recursive(dynamic, T, V, l, max_q, i, q):
    if T[i] + q >= l:
        dynamic[i][q] = 0
        return 0

    if i == len(T) - 1:
        if min(q + V[i], max_q) + T[i]>= l:
            dynamic[i][q] = 1
            return 1
        else:
            dynamic[i][q] = float('inf')
            return float('inf')

    if dynamic[i][q] != -1:
        return dynamic[i][q]

    before_g = q
    q = min(V[i] + q, max_q)
    idx = i + 1
    minimum = float('inf')
    while idx < len(T) and T[idx] <= q + T[i]:
        val = recursive(dynamic, T, V, l, max_q, idx, q - T[idx] + T[i])
        #dynamic[idx][q - T[idx] + T[i]] = val
        if val < minimum:
            minimum = val
        idx += 1
    dynamic[i][before_g] = minimum + 1
    return minimum + 1

runtests( iamlate )

T =  [0, 5, 10]
V =  [10, 5, 20]
q =  100
l =  35

#print(iamlate(T, V, q, l))