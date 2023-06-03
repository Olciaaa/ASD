from egzP6btesty import runtests 

def jump ( M ):
    status = makingJumps(M)
    toReturn = 0
    for el in status.values():
        if el:
            toReturn += 1
    #tutaj proszę wpisać własną implementację
    return toReturn

def makingJumps(M):
    x = 0
    y = 0
    moves = {(x,y):True}

    for el in M:
        x, y = changePos(2, el[0], x, y)
        x, y = changePos(1, el[1], x, y)

        val = moves.get((x, y))
        if val is None:
            moves.update({(x, y): True})
        else:
            moves[(x, y)] = not val
    return moves

def changePos(val, key, x, y):
    if key == 'L':
        x -= val
    elif key == 'R':
        x += val
    elif key == 'U':
        y += val
    else:
        y -= val

    return x, y
runtests(jump, all_tests = True)