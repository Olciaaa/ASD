def next(arr, target):
    start = 0
    end = len(arr) - 1
 
    ans = -1
    while (start <= end):
        mid = (start + end) // 2

        if (arr[mid] <= target):
            start = mid + 1

        else:
            ans = mid
            end = mid - 1
 
    return ans