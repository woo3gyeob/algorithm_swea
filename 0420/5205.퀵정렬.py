def quickSort(arr, lo, hi):
    if lo < hi:
        i, j = lo, hi

        while i < j:
            while i <= hi and arr[i] <= arr[lo]:
                i += 1

            while arr[j] > arr[lo]:
                j -= 1

            if i >= j: break

            arr[i], arr[j] = arr[j], arr[i]

        arr[lo], arr[j] = arr[j], arr[lo]

        quickSort(arr, lo, j - 1)
        quickSort(arr, j + 1, hi)


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, n - 1)
    print('#%d %d' %(tc, arr[n//2]))
