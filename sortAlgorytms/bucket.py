def insertionSort(tab, n):
    for i in range(n):
        key = tab[i]
        j = i - 1

        while(j >= 0 and tab[j] > key):
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key


def bucket(tab, max_val, min_val, n):
    sequence = (max_val - min_val) / n + 0.5
    buckets = [[] for _ in range(n)]
    sortedTab = []

    for el in tab:
        bucket_id = int((el - min_val) / sequence)
        buckets[bucket_id].append(el)

    for bucket in buckets:
        insertionSort(bucket, len(bucket))
        for el in bucket:
            sortedTab.append(el)
    return sortedTab

tab = [3, 5, 6, 8, 1, 3, 6, 7]
print(bucket(tab, 8, 1, len(tab)))