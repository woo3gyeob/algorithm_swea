def perm(idx, power, cnt):
    global min_cnt
    if cnt >= min_cnt:
        return
    power -= 1
    if power >= n - idx - 1:
        min_cnt = cnt
        return
    perm(idx + 1, arr[idx], cnt + 1)
    if power != 0:
        perm(idx + 1, power, cnt)


for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    min_cnt = 200
    perm(1, arr[0], 0)
    print('#%d %d' % (tc, min_cnt))