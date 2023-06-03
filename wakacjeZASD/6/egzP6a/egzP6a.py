from egzP6atesty import runtests 
#97, 122
def google ( H, s ):
    #tutaj proszę wpisać własną implementację

    for i in range(len(H)):
        H[i] = [H[i], numOfLetters(H[i])]

    tab = bucketSort(H)
    tab.reverse()
    idxOfBucket = 0
    curr = 0
    for i in range(len(tab)):

        if s <= curr + len(tab[i]):
            idxOfBucket = i
            break
        curr += len(tab[i])

    return bucketSort1(tab[idxOfBucket])[s - curr - 1]

def numOfLetters(word):
    letters = 0

    for i in range(len(word)):
        if ord(word[i]) >= 97 and ord(word[i]) <= 122:
            letters += 1

    return letters

def bucketSort(H):
    maxlen = 0
    for el in H:
        maxlen = max(maxlen, len(el[0]))
    tab = [[] for _ in range(maxlen + 1)]

    for el in H:
        tab[len(el[0])].append((el[1], el[0]))

    return tab

def bucketSort1(H):
    maxlen = 0
    for el in H:
        maxlen = max(maxlen, el[0])
    tab = [[] for _ in range(maxlen + 1)]

    for el in H:
        tab[el[0]].append(el[1])

    toReturn = []
    for el in tab:
        for ell in el:
            toReturn.append(ell)
    toReturn.reverse()

    return toReturn

runtests ( google, all_tests=True )