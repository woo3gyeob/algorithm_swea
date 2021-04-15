def perm(idx, val):
    global min_val
    if sum(visited) == n:
        if val < min_val:
            min_val = val
        return

    if sum(visited) == n - 1:
        visited[0] = 1
        perm(0, val + arr[idx][0])
        visited[0] = 0

    else:
        for i in range(1, n):
            if not visited[i]:
                visited[i] = 1
                sum_val = val + arr[idx][i]
                perm(i, sum_val)
                visited[i] = 0


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_val = 987654321
    perm(0, 0)
    print('#%d %d' % (tc, min_val))