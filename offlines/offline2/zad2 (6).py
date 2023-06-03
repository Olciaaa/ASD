from zad2testy import runtests

def partitionspecialdol(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if (A[j])[0]< x[0]:
            i+=1
            A[i],A[j]=A[j],A[i]
        elif (A[j])[0]==x[0]:
            if x[1]<(A[j])[1]:
                i+=1
                A[i], A[j] = A[j], A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quicksortspecialdol(A,p,r):
    while p<r:
        q=partitionspecialdol(A,p,r)
        quicksortspecialdol(A,p,q-1)
        #quicksortspecialdol(A,q+1,r)
        p=q+1


def depth(L):
    dl=len(L)
    quicksortspecialdol(L, 0, dl - 1)
    k = 0
    next = 0
    best = 0
    wsk = 1
    while wsk<dl and dl - best > wsk:
        count = 0
        no=L[k]
        while no[1] > (L[wsk])[0] and wsk < dl - 1:
            if no[1] >= (L[wsk])[1]:
                count += 1
            else:
                if no[0] != (L[wsk])[0] and next == k:
                    next = wsk
            wsk += 1
        if no[1] >= (L[wsk])[1]:
            count += 1
        if count > best:
            best = count
        if next == k:
            break
        else:
            k = next
            wsk = next + 1
    return best

runtests( depth ) 
