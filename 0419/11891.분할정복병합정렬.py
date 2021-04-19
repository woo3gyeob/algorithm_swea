def mergeSort(s, e):
    global cnt
    if e - s < 1: return
    # 분할하기
    # mid = (s + e) >> 1
    mid = (s + e + 1) // 2
    l = mergeSort(s, mid - 1)
    r = mergeSort(mid, e)

    if arr[mid - 1] > arr[e]:
        cnt += 1

    i, j, k = s, mid, s
    while i < mid and j <= e:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1

    while i < mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= e:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1

    for i in range(s, e + 1):
        arr[i] = tmp[i]


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * n
    cnt = 0
    mergeSort(0, n - 1)
    print('#%d %d %d' % (tc, arr[n // 2], cnt))