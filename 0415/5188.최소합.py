def perm(r, c, sum_val):
    global min_val
    if r == n - 1 and c == n - 1:
        if sum_val < min_val:
            min_val = sum_val
            return

    if sum_val > min_val:
        return

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr > -1 and nr < n and nc > -1 and nc < n:
            perm(nr, nc, sum_val + arr[nr][nc])


dr = [1, 0]
dc = [0, 1]

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_val = 987654321
    perm(0, 0, arr[0][0])
    print('#%d %d' % (tc, min_val))