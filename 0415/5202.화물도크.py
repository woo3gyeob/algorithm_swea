def move(idx, cnt, start):
    global max_cnt
    if idx == 24 or start == n - 1:
        if max_cnt < cnt:
            max_cnt = cnt
        return

    for i in range(start, n):
        if idx <= arr[i][0]:
            move(arr[i][1], cnt + 1, i)


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: [x[0], x[1]])
    max_cnt = 0
    move(0, 0, 0)
    print('#%d %d' % (tc, max_cnt))