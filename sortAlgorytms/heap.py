def heapify(tab, broken_id, n):
    left_id = broken_id * 2 + 1
    right_id = broken_id * 2 + 2
    max_id = broken_id

    if left_id < n and tab[left_id] > tab[max_id]:
        max_id = left_id

    if right_id < n and tab[right_id] > tab[max_id]:
        max_id = right_id

    if broken_id != max_id:
        tab[max_id], tab[broken_id] = tab[broken_id], tab[max_id]
        heapify(tab, max_id, n)

def heapSort(tab):
    n = len(tab)
    for i in range(n // 2 - 1, -1, -1):
        heapify(tab, i, n)

    for i in range(n - 1, -1, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab,0 ,i)

tab = [2, 4,6, 7,567,2, 43, 2,1]
heapSort(tab)
print(tab)