from zad8ktesty import runtests 

def napraw ( s, t ):
    print(s)
    print(t)
    dynamic = [[-1 for _ in range(len(t))] for _ in range(len(s))]
    val = recursive(s, t, dynamic, len(s) - 1, len(t) - 1)
    for el in dynamic:
        print(el)
    return val

def recursive(bad_name, name, dynamic, idx_in_bad, idx_in_good):
    if idx_in_good == -1 or idx_in_bad == -1:
        return abs(idx_in_good - idx_in_bad)

    if dynamic[idx_in_bad][idx_in_good] != -1:
        return dynamic[idx_in_bad][idx_in_good]

    if bad_name[idx_in_bad] == name[idx_in_good]:
        dynamic[idx_in_bad][idx_in_good] = recursive(bad_name, name, dynamic, idx_in_bad - 1, idx_in_good - 1)
        return dynamic[idx_in_bad][idx_in_good]
    dynamic[idx_in_bad][idx_in_good] = min(recursive(bad_name, name, dynamic, idx_in_bad - 1, idx_in_good - 1), recursive(bad_name, name, dynamic, idx_in_bad, idx_in_good - 1), recursive(bad_name, name, dynamic, idx_in_bad - 1, idx_in_good)) + 1
    return dynamic[idx_in_bad][idx_in_good]
runtests ( napraw )