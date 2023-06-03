from egzP8atesty import runtests 

def reklamy ( T, S, o ):
    #print(T)
    #print(S)
    #print(o)
    for i in range(len(T)):
        T[i] = [T[i], S[i]]
    T.sort(key = lambda x: x[0][0])
#    print(T)
    dict, keys = makeDict(T)
    keys.reverse()

    maximum = 0
    for i in range(len(T)):
        id = T[i][0][1] + 1
        if dict.get(id) is None:
            id = next(keys, id)
        maximum = max(dict[id] + T[i][1], maximum)
    #Tutaj proszę wpisać własną implementację 
    return maximum


def next(arr, target):
    start = 0
    end = len(arr) - 1

    ans = -1
    while (start <= end):
        mid = (start + end) // 2

        # Move to right side if target is
        # greater.
        if (arr[mid] <= target):
            start = mid + 1

        # Move left side.
        else:
            ans = mid
            end = mid - 1

    return arr[ans]

def makeDict(T):
    dict = {}
    keys = []
    currMax = 0
    for i in range(len(T) - 1, -1, -1):
        if dict.get(T[i][0][0]) is None:
            keys.append(T[i][0][0])
        currMax = max(currMax, T[i][1])
        dict[T[i][0][0]] = currMax
    return dict, keys

runtests ( reklamy, all_tests=True )