def cutlist(L):
    if L is None:
        return None
    while L.next is not None and L.next.value >= L.value:
        L = L.next
    H = L.next
    L.next = None
    return H, L # L to ogon

def mergesort(L):
    while True:
        NH = None
        NT = None
        while True:

            if L == None:
                L = NH
                break
            A = L
            L, T = cutlist(L)

            if NT == None and L == None:
                return A
            if L == None:
                NT.next = A
                L = NH
                break
            B = L
            L, _ = cutlist(L)


            X, T = merge(A,B)

            if NH == None:
                NH = X
            else:
                NT.next = X
            NT = T