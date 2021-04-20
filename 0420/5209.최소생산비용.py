def perm(idx, sum_val):
    global min_val
    if sum_val >= min_val:
        return
    if idx == n:
        min_val = sum_val
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            perm(idx+1, sum_val + arr[idx][i])
            visited[i] = 0

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_val = 987654321
    perm(0, 0)
    print('#%d %d' %(tc, min_val))