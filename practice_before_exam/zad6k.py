from zad6ktesty import runtests 

def haslo ( S ):
    print(S)
    tab = ["00", "30","40", "50", "60", "70", "80", "90"]
    for i in range(1, len(S)):
        for el in tab:
            if S[i - 1: i + 1] == el:
                return 0

    return recursive(S, len(S) - 1)


def canBeWord(S):
    if S[0] == "0":
        return False
    if int(S) <= 26:
        #print(S)
        return True
    return False

def recursive(S, idx):
    if idx <= 0:
        return 1

    if S[idx] == "0":
        #print(idx)
        return recursive(S, idx - 2)

    if idx + 1 < len(S) and S[idx + 1] == "0":
        #print(idx)
        return recursive(S, idx + 1)

    if canBeWord(S[idx - 1: idx + 1]):
        return recursive(S, idx - 1) + recursive(S, idx - 2)
    return recursive(S, idx - 1)

runtests ( haslo )
#print(haslo("12345"))