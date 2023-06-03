'''
najdłuższy rosnący podciąg
'''

def maximum_length(tab):
    dynamic = [0 for _ in range(len(tab))]

    curr_max = 1
    for i in range(len(tab)):
        curr = recursive(tab, i, dynamic)
        if curr > curr_max:
            curr_max = curr

    print(dynamic)
    return curr_max

def recursive(tab, idx, dynamic):
    if idx == len(tab):
        return 0

    for i in range(idx + 1, len(dynamic)):
        if tab[idx] < tab[i] and dynamic[i] != 0:
            return dynamic[i]

    curr_max = 0
    for i in range(idx + 1, len(tab)):
        curr = 0
        if tab[idx] < tab[i]: curr = recursive(tab, i, dynamic)
        if curr > curr_max:
            curr_max = curr

    dynamic[idx] = curr_max + 1
    return curr_max + 1

tab = [2,4,2,7,2,65,1]
print(maximum_length(tab))