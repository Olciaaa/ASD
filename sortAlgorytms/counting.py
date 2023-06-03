def counting(tab, n, max_el):
    counts = [0 for _ in range(max_el)]
    sorted = [0 for _ in range(n)]

    for i in range(n):
        counts[tab[i]] += 1

    for i in range(1, max_el):
        counts[i] += counts[i - 1]

    for i in range(n - 1, -1, -1):
        sorted[counts[tab[i]] - 1] = tab[i]
        counts[tab[i]] -= 1

    return sorted

tab = [3, 1, 4, 3, 1, 3, 2, 1, 8]
print(counting(tab, len(tab), 9))