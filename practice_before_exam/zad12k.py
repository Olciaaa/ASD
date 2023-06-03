from zad12ktesty import runtests 

def autostrada( T, k ):
    dynamic = [[-1 for _ in range(k + 1)] for _ in range(len(T))]

    return (recursive(T, dynamic, k, 0, 1))

def recursive(T, dynamic, k, idx, current_k):
    if idx == len(T):
        return 0

    if dynamic[idx][current_k] != -1:
        return dynamic[idx][current_k]

    if current_k == k:
        value = 0
        for i in range(idx, len(T)):
            value += T[i]
        dynamic[idx][current_k] = value
        return value


    value = T[idx]
    minimum = float('inf')
    for i in range(idx + 1, len(T)):
        curr = max(recursive(T, dynamic, k, i, current_k + 1), value)
        value += T[i]

        if minimum > curr:
            minimum = curr

    dynamic[idx][current_k] = minimum
    return minimum

runtests ( autostrada,all_tests=True )