def bisect_left(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo


print(bisect_right([0, 3, 3, 3, 3, 4, 6, 9, 10], 3))
print(bisect_left([0, 3, 3, 3, 3, 4, 6, 9, 10], 3))
